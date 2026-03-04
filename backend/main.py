import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sentiment_predictor import SentimentPredictor

app = FastAPI(title="AI Sentiment Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Determine model path dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "sentiment_model.pkl")
predictor = SentimentPredictor(model_path=MODEL_PATH)

class PredictionRequest(BaseModel):
    user_text: str

class PredictionResponse(BaseModel):
    sentiment: str
    confidence: float
    scores: dict

@app.post("/predict", response_model=PredictionResponse)
def predict_sentiment(req: PredictionRequest):
    result = predictor.predict(req.user_text)
    return PredictionResponse(
        sentiment=result["sentiment"],
        confidence=result["confidence"],
        scores=result["scores"]
    )

@app.get("/health")
def health_check():
    return {"status": "ok"}
