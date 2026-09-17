# Churn Prediction API

Live API: https://my-api-jq1g.onrender.com/docs

Predicts if a customer will churn (leave) or not.

## Tech Stack
- Python, FastAPI, Scikit-learn
- Deployed on Render

## How to use API
POST /predict
Sample JSON:
{
  "tenure": 12,
  "MonthlyCharges": 70.5,
  "TotalCharges": 800,
  "Contract": "Month-to-month"
}

## Run Locally
pip install -r requirements.txt
uvicorn main:app --reload
