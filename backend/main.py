import os
import sys
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sentiment_predictor import SentimentPredictor

app = FastAPI(title="AI Sentiment Analyzer Pro API")

# Add Prometheus Monitoring middleware
# This adds /metrics endpoint
Instrumentator().instrument(app).expose(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load deep learning model
predictor = SentimentPredictor()

class PredictionRequest(BaseModel):
    user_text: str

class PredictionResponse(BaseModel):
    sentiment: str
    confidence: float
    scores: dict
    version: str

@app.post("/predict", response_model=PredictionResponse)
def predict_sentiment(req: PredictionRequest):
    result = predictor.predict(req.user_text)
    return PredictionResponse(
        sentiment=result["sentiment"],
        confidence=result["confidence"],
        scores=result["scores"],
        version=result["version"]
    )

# Real-time WebSocket Stream for Inference
import asyncio

@app.websocket("/ws/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # Task to simulate massive incoming data stream
    async def simulate_social_media():
        mock_tweets = [
            "Just deployed a huge feature to production, feels good!",
            "Terrible customer service from this brand today :( never using them again",
            "What a beautiful morning to grab coffee",
            "This software is absolutely broken, fixing bugs for 5 hours straight",
            "Neutral statement about the upcoming event at 6pm"
        ]
        while True:
            await asyncio.sleep(3)
            import random
            tweet = random.choice(mock_tweets)
            result = predictor.predict(tweet)
            response = {
                "original_text": f"[LIVE EVENT] {tweet}",
                "sentiment": result["sentiment"],
                "confidence": result["confidence"],
                "scores": result["scores"],
                "version": result["version"]
            }
            await websocket.send_text(json.dumps(response))

    task = asyncio.create_task(simulate_social_media())
    
    try:
        while True:
            text = await websocket.receive_text()
            result = predictor.predict(text)
            response = {
                "original_text": text,
                "sentiment": result["sentiment"],
                "confidence": result["confidence"],
                "scores": result["scores"],
                "version": result["version"]
            }
            await websocket.send_text(json.dumps(response))
    except WebSocketDisconnect:
        task.cancel()
        print("Client disconnected from inference stream.")

@app.get("/health")
def health_check():
    return {"status": "ok"}
