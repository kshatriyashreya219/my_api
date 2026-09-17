from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(
    title="Churn Prediction API",
    description="Customer Churn Prediction",
    version="1.0"
)

# Load Model - supports both joblib and pickle
try:
    model = joblib.load("churn_model.pkl")
    print("Model loaded via joblib")
except:
    import pickle
    with open("churn_model.pkl", "rb") as f:
        model = pickle.load(f)
    print("Model loaded via pickle")

@app.get("/")
def root():
    return {
        "status": "API is Live",
        "model_loaded": True,
        "message": "Go to /docs for testing"
    }

@app.post("/predict")
def predict_churn(data: dict):
    """
    Send your model features as JSON
    Example: {"tenure": 12, "MonthlyCharges": 70.5,...}
    """
    try:
        # Convert incoming json to dataframe
        df = pd.DataFrame([data])
        prediction = model.predict(df)
        prediction_value = int(prediction[0])

        result = "Customer will Churn" if prediction_value == 1 else "Customer will NOT Churn"

        return {
            "prediction": prediction_value,
            "result": result
        }
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Make sure you are sending same columns as used in training"
        }