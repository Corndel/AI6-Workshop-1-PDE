import json, pathlib, tarfile, joblib, pandas as pd, xgboost
from sklearn.metrics import roc_auc_score

#Corndel Level 6 AI/ML Engineer Workshop 1
#Evaluate Stage Script
#Note that the /opt/ml/ paths are automagically created by SageMaker

test_data_path = "/opt/ml/processing/test/validation.csv"
output_dir = "/opt/ml/processing/evaluation"
model_path = "/opt/ml/processing/model/model.tar.gz"


if __name__ == "__main__":
    with tarfile.open(model_path, "r:gz") as tar:
        tar.extractall("./model")
    model = joblib.load("./model/xgboost-model")

    df = pd.read_csv(test_data_path, header=None)

    y_test = df.iloc[:, 0].to_numpy()
    df.drop(df.columns[0], axis=1, inplace=True)
    X_test = xgboost.DMatrix(df.values)

    predictions = model.predict(X_test)
    auc = roc_auc_score(y_test, predictions)

    evaluation_report = {"regression_metrics": {"auc": {"value": auc}}}

    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
    with open(f"{output_dir}/evaluation.json", "w") as f:
        f.write(json.dumps(evaluation_report))
