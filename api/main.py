'''
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
'''

from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response
import time
 
app = FastAPI()
 
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests"
)
 
REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency"
)
 
@app.get("/")
def root():
    REQUEST_COUNT.inc()
    return {"message": "FastAPI is running"}
 
@app.get("/predict")
def predict():
    start = time.time()
    time.sleep(0.2)  # simulate model inference
    REQUEST_LATENCY.observe(time.time() - start)
    return {"prediction": 123}
 
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")