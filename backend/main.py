from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from typing import List
import os

# Fix: Get absolute path regardless of where you run from
BASE_DIR = Path(__file__).resolve().parent.parent  # Goes up to ecommerce-intelligence/
MODELS_PATH = BASE_DIR / "ml" / "models"

print(f"Looking for models in: {MODELS_PATH}")

# Initialize FastAPI
app = FastAPI(title="E-commerce Intelligence API")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if models exist before loading
if not MODELS_PATH.exists():
    raise Exception(f"Models directory not found at {MODELS_PATH}")

# Load models
try:
    fraud_model = joblib.load(MODELS_PATH / "fraud_model.pkl")
    fraud_scaler = joblib.load(MODELS_PATH / "fraud_scaler.pkl")
    print("✅ Fraud model loaded")
except FileNotFoundError as e:
    print(f"❌ Fraud model not found: {e}")
    print("Please run: cd ml && python train.py first")
    raise

try:
    sales_model = joblib.load(MODELS_PATH / "sales_model.pkl")
    sales_scaler = joblib.load(MODELS_PATH / "sales_scaler.pkl")
    print("✅ Sales model loaded")
except FileNotFoundError as e:
    print(f"❌ Sales model not found: {e}")
    raise

try:
    segment_model = joblib.load(MODELS_PATH / "segment_model.pkl")
    segment_scaler = joblib.load(MODELS_PATH / "segment_scaler.pkl")
    print("✅ Segmentation model loaded")
except FileNotFoundError as e:
    print(f"❌ Segmentation model not found: {e}")
    raise

print("🎉 All models loaded successfully!")

# Request/Response Schemas
class FraudRequest(BaseModel):
    features: List[float]

class FraudResponse(BaseModel):
    is_fraud: bool
    probability: float

class SalesRequest(BaseModel):
    features: List[float]

class SalesResponse(BaseModel):
    predicted_sales: float

class SegmentRequest(BaseModel):
    features: List[float]

class SegmentResponse(BaseModel):
    segment: int
    segment_name: str

# API Endpoints
@app.get("/")
def root():
    return {"message": "E-commerce Intelligence API", "status": "running"}

@app.post("/predict/fraud", response_model=FraudResponse)
def predict_fraud(request: FraudRequest):
    """Predict if transaction is fraudulent"""
    try:
        features = np.array(request.features).reshape(1, -1)
        features_scaled = fraud_scaler.transform(features)
        probability = fraud_model.predict_proba(features_scaled)[0, 1]
        is_fraud = probability > 0.5
        return FraudResponse(is_fraud=is_fraud, probability=float(probability))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict/sales", response_model=SalesResponse)
def predict_sales(request: SalesRequest):
    """Predict sales based on features"""
    try:
        features = np.array(request.features).reshape(1, -1)
        features_scaled = sales_scaler.transform(features)
        prediction = sales_model.predict(features_scaled)[0]
        return SalesResponse(predicted_sales=float(prediction))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/segment/customer", response_model=SegmentResponse)
def segment_customer(request: SegmentRequest):
    """Segment customer into group"""
    try:
        features = np.array(request.features).reshape(1, -1)
        features_scaled = segment_scaler.transform(features)
        segment = segment_model.predict(features_scaled)[0]
        
        segment_names = {
            0: "High Value",
            1: "At Risk",
            2: "Bargain Hunter",
            3: "New Customer"
        }
        
        return SegmentResponse(
            segment=int(segment),
            segment_name=segment_names.get(segment, "Unknown")
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)