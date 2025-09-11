import sagemaker
import boto3
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.processing import ScriptProcessor, ProcessingInput, ProcessingOutput
from sagemaker.workflow.steps import ProcessingStep
from sagemaker.estimator import Estimator
from sagemaker.workflow.steps import TrainingStep
from sagemaker.workflow.properties import PropertyFile
from sagemaker.model import Model
from sagemaker.workflow.model_step import ModelStep
from sagemaker.workflow.conditions import ConditionGreaterThanOrEqualTo
from sagemaker.workflow.condition_step import ConditionStep
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.inputs import TrainingInput
from sagemaker.workflow.step_collections import RegisterModel
from sagemaker.workflow.functions import JsonGet

#Corndel Level 6 AI/ML Engineer
#Amazon SageMaker Pipeline Deployment Stage


def get_account_id():
    sts_client = boto3.client("sts")
    identity = sts_client.get_caller_identity()
    return identity["Account"]


# --- IMPORTANT --- 
# Ensure the cs-training.csv file is in this S3 location.
input_data_s3_uri = f"s3://quickloan-ml-us-east-1-{get_account_id()}/input/cs-training.csv"



def run_pipeline():
    """Defines and executes the SageMaker ML Pipeline."""
    
    # 1. Setup: Roles, Sessions, and S3 Locations
    sagemaker_role = sagemaker.get_execution_role()
    region = boto3.Session().region_name
    pipeline_session = PipelineSession()
    default_bucket = pipeline_session.default_bucket()
    base_job_prefix = "quickloan-pipeline"
        
    print(f"Using SageMaker Role: {sagemaker_role}")
    print(f"Using S3 Bucket: {default_bucket}")

    # 2. Pipeline Step: Data Processing
    script_processor = ScriptProcessor(
        command=["python3"],
        image_uri=sagemaker.image_uris.retrieve("sklearn", region, "0.23-1"),
        instance_type="ml.m5.large",
        instance_count=1,
        base_job_name=f"{base_job_prefix}/data-processing",
        sagemaker_session=pipeline_session,
        role=sagemaker_role,
    )
    step_process = ProcessingStep(
        name="QuickLoanProcessData",
        processor=script_processor,
        inputs=[ProcessingInput(source=input_data_s3_uri, destination="/opt/ml/processing/input")],
        outputs=[
            ProcessingOutput(output_name="train", source="/opt/ml/processing/train"),
            ProcessingOutput(output_name="validation", source="/opt/ml/processing/validation"),
        ],
        code="src/process.py",
    )

    # 3. Pipeline Step: Model Training
    xgb_estimator = Estimator(
        image_uri=sagemaker.image_uris.retrieve("xgboost", region, "1.5-1"),
        instance_type="ml.m5.xlarge",
        instance_count=1,
        role=sagemaker_role,
        sagemaker_session=pipeline_session,
        hyperparameters={"objective": "binary:logistic", "num_round": 200}
    )
    step_train = TrainingStep(
        name="QuickLoanTrainModel",
        estimator=xgb_estimator,
        inputs={
            "train": TrainingInput(s3_data=step_process.properties.ProcessingOutputConfig.Outputs["train"].S3Output.S3Uri),
            "validation": TrainingInput(s3_data=step_process.properties.ProcessingOutputConfig.Outputs["validation"].S3Output.S3Uri)
        }
    )

    # 4. Pipeline Step: Model Evaluation
    evaluation_report = PropertyFile(name="EvaluationReport", output_name="evaluation", path="evaluation.json")
    script_evaluator = ScriptProcessor(
        command=["python3"],
        image_uri=sagemaker.image_uris.retrieve("sklearn", region, "0.23-1"),
        instance_type="ml.m5.large",
        instance_count=1,
        role=sagemaker_role,
        sagemaker_session=pipeline_session,
    )
    step_evaluate = ProcessingStep(
        name="QuickLoanEvaluateModel",
        processor=script_evaluator,
        inputs=[
            ProcessingInput(source=step_train.properties.ModelArtifacts.S3ModelArtifacts, destination="/opt/ml/processing/model"),
            ProcessingInput(source=step_process.properties.ProcessingOutputConfig.Outputs["validation"].S3Output.S3Uri, destination="/opt/ml/processing/test")
        ],
        outputs=[ProcessingOutput(output_name="evaluation", source="/opt/ml/processing/evaluation")],
        code="src/evaluate.py",
        property_files=[evaluation_report]
    )

    # 5. Pipeline Step: Conditional Model Registration
    model_package_group_name = "QuickLoanCreditRiskModels"
    
    # --- CORRECTED CODE BLOCK ---
    # Use the RegisterModel step for registering the model package
    step_register = RegisterModel(
        name="RegisterQuickLoanModel",
        estimator=xgb_estimator,
        model_data=step_train.properties.ModelArtifacts.S3ModelArtifacts,
        content_types=["text/csv"],
        response_types=["text/csv"],
        inference_instances=["ml.t2.medium", "ml.m5.large"],
        transform_instances=["ml.m5.xlarge"],
        model_package_group_name=model_package_group_name,
        approval_status="PendingManualApproval"
    )
    
    condition_gte = ConditionGreaterThanOrEqualTo(
        left=JsonGet(
            step_name=step_evaluate.name,
            property_file=evaluation_report,
            json_path="regression_metrics.auc.value"
        ),
        right=0.75,  # AUC Threshold
    )
    
    step_conditional_register = ConditionStep(
        name="CheckAUCAndRegister",
        conditions=[condition_gte],
        if_steps=[step_register],
        else_steps=[],
    )

    # 6. Assemble and Run the Pipeline
    pipeline_name = "QuickLoan-Ethics-First-Pipeline"
    pipeline = Pipeline(
        name=pipeline_name,
        steps=[step_process, step_train, step_evaluate, step_conditional_register],
        sagemaker_session=pipeline_session,
    )
    
    print(f"Creating/updating pipeline: {pipeline_name}")
    pipeline.upsert(role_arn=sagemaker_role)
    
    print("Starting pipeline execution...")
    execution = pipeline.start()
    print(f"Pipeline execution started: {execution.arn}")
    
if __name__ == "__main__":
    run_pipeline()
