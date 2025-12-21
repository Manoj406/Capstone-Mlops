import onnxruntime as ort
import numpy as np
 
MODEL_PATH = "/home/user16/capstone-mlops/models/california_housing.onnx"
 
def load_model():
    session = ort.InferenceSession(MODEL_PATH)
    input_name = session.get_inputs()[0].name
    return session, input_name
 
session, input_name = load_model()
 
def predict(features):
    input_array = np.array(features, dtype=np.float32).reshape(1, -1)
    outputs = session.run(None, {input_name: input_array})
    return float(outputs[0][0])
