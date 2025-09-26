# Model Card: QuickLoan Credit Scoring Model

This model card provides information about the machine learning model developed for the fictional "QuickLoan" company as part of the AI6-Workshop-1-PDE.

## Model Details

* **Model Name**: QuickLoan Credit Scoring Model
* **Version**: 1.0
* **Developers**: Participants of the Level 6 AI/ML Engineer Programme
* **Model Date**: 2025-09-26
* **Model Type**: Gradient Boosted Trees (XGBoost) for Binary Classification
* **Contact**: AI Governance Team <ai-governance@quickloan-fictional.com>

---

## Intended Use

* **Primary Use**: To predict the probability of a loan applicant defaulting on a loan. This model is intended to be used as a **decision-support tool** for human loan officers at the "QuickLoan" company to aid in their risk assessment process.
* **Intended Users**: Loan Officers, Credit Risk Analysts.

### 🚫 Out-of-Scope Uses

This model is **NOT** intended for:
* Fully automated loan approval or denial without human oversight.
* Determining loan interest rates or credit limits.
* Use in marketing, customer profiling, or any purpose other than credit risk assessment.
* Use by any entity other than the "QuickLoan" company. The model is a protected corporate asset.

---

## Training Data

* **Dataset**: `cs-training.csv`
* **Description**: The model was trained on a dataset containing historical financial information from past loan applicants. The data includes various financial attributes and a target variable indicating whether the applicant defaulted.
* **Preprocessing**: A preprocessing step (`src/process.py`) running in a `scikit-learn:0.23-1` container was executed within the SageMaker Pipeline. This step cleans the data and splits it into training and validation sets.
* **Data Sensitivity**: The dataset contains sensitive financial information. While personally identifiable information (PII) is assumed to be removed, the data is subject to privacy regulations like **GDPR**. The model itself is considered a derivative of this sensitive data.

---

## Training Procedure

The model was trained as part of an automated AWS SageMaker Pipeline (`QuickLoan-Ethics-First-Pipeline`).

* **Algorithm**: XGBoost (version `1.5-1`)
* **Objective Function**: `binary:logistic`
* **Hyperparameters**: `num_round: 200`
* **Infrastructure**:
    * **Data Processing**: `ml.m5.large` AWS SageMaker instance.
    * **Model Training**: `ml.m5.xlarge` AWS SageMaker instance.
* **Model Governance**: Upon successful evaluation, the model is automatically registered to the `QuickLoanCreditRiskModels` SageMaker Model Package Group with an approval status of **`PendingManualApproval`**. This ensures a human review must occur before the model can be deployed.

---

## Evaluation

* **Evaluation Script**: Model performance was assessed using the `src/evaluate.py` script on the held-out validation set.
* **Performance Metric**: The primary metric used to determine model quality for registration is the **Area Under the ROC Curve (AUC)**.
* **Threshold**: The pipeline includes a conditional step that only registers the model if its performance meets a minimum threshold: $AUC \ge 0.75$.
* **Evaluation Report**: A full evaluation report (`evaluation.json`) is generated, which may contain other metrics like Accuracy, Precision, and Recall. This report is used by the governance team during the manual approval step.

---

## Ethical Considerations and Limitations

This model is considered a **regulated asset** and is subject to multiple policies and regulations.

* **Fairness and Bias**: ⚖️ Financial models are subject to fairness regulations (e.g., from the UK's Financial Conduct Authority). The training data may contain historical biases that the model could learn and amplify. **This initial version of the model has not undergone a formal bias audit.** It is crucial to analyze the model's predictions across protected characteristics (e.g., age, gender, ethnicity) before deployment to ensure equitable outcomes.
* **Explainability**: As a financial model, its decisions cannot be a "black box." The `model.tar.gz` artifact must be accompanied by explainability reports (e.g., SHAP values) to justify individual predictions to customers and regulators.
* **Data Privacy**: 🔒 The model is a derivative of sensitive data. Access to the model artifact (`model.tar.gz`) and the underlying training data must be strictly controlled to prevent reverse-engineering that could expose information about individuals in the training set, in compliance with GDPR.
* **Intellectual Property**: 💼 The trained model is a valuable trade secret of the "QuickLoan" company. Its distribution and access are restricted by internal corporate policy.

## Caveats and Recommendations

* This model should always be used with human oversight.
* Continuous monitoring for performance drift and fairness degradation must be implemented post-deployment.
* Before any deployment, the model must pass the `PendingManualApproval` stage, which should include a thorough review of its performance and fairness metrics by a dedicated risk and governance team.
