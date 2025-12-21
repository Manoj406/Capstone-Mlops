from pydantic import BaseModel
from typing import List
 
class HousingInput(BaseModel):
    features: List[float]
 
class PredictionOutput(BaseModel):
    prediction: float
