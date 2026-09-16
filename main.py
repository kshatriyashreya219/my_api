from fastapi import dFastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI(title="Vehicle Traffic Prediction API")

# Model load karne ka try karega. Nahi mila to dummy chalega
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    model = None

class TrafficInput(BaseModel):
    junction: int
    hour: int
    day: int
    is_holiday: int

@app.get("/")
def read_root():
    return {"message": "Traffic Prediction API is running"}

@app.post("/predict")
def predict_traffic(data: TrafficInput):
    if model is None:
        # Dummy prediction agar model nahi hai
        prediction = 150 + data.hour * 10 + data.junction * 5
    else:
        input_df = pd.DataFrame([data.dict()])
        prediction = model.predict(input_df)[0]
    
    if prediction > 200:
        congestion = "High"
    elif prediction > 100:
        congestion = "Medium"
    else:
        congestion = "Low"
        
    return {
        "predicted_vehicle_count": int(prediction),
        "congestion_level": congestion
    }