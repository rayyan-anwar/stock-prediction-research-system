from fastapi import FastAPI,HTTPException
from backend.app.schemas import ForecastRequest,ForecastResponse
from backend.app.model import forecast

app=FastAPI(title="Rayyan Anwar | Stock Prediction Research API",
 description="Financial time-series research service by Rayyan Anwar.")

@app.get("/health")
def health():
    return {"status":"ok","author":"Rayyan Anwar","service":"stock-prediction-research"}

@app.post("/api/v1/forecast",response_model=ForecastResponse)
def predict(req:ForecastRequest):
    try: pred,direction=forecast([[x.close,x.volume] for x in req.prices])
    except ValueError as e: raise HTTPException(status_code=400,detail=str(e))
    return ForecastResponse(author="Rayyan Anwar",next_price_estimate=pred,
      direction=direction,methodology="Lagged price/return/volume features with Random Forest and chronological evaluation.")
