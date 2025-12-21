import mlflow
import mlflow.sklearn
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

mlflow.set_tracking_uri("http://localhost:5001")
model_uri="models:/California_Housing_Model/latest"

model=mlflow.sklearn.load_model(model_uri)
initial_type=[("input",FloatTensorType([None,8]))]

onnx_model=convert_sklearn(model,initial_types=initial_type)

onnx_path="models/california_housing.onnx"
with open(onnx_path,"wb") as f:
	f.write(onnx_model.SerializeToString())
print("ONNX model saved")

with mlflow.start_run(run_name="onnx-conversion"):
	mlflow.log_artifact(onnx_path,artifact_path="onnx_model")
print("ONNX model logged to mlflow")
