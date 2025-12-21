from fastapi import FastAPI
from api.schema import HousingInput, PredictionOutput
from api.model_loader import predict
 
app = FastAPI(title="California Housing Inference API")
 
@app.get("/")
def health():
    return {"status": "API is running"}
 
@app.post("/predict", response_model=PredictionOutput)
def make_prediction(data: HousingInput):
    result = predict(data.features)
    return {"prediction": result}
