from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
import re
import random

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

class SentimentPredictor:
    def __init__(self):
        print(f"Loading Model A (DistilBERT)...")
        self.model_A = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        
        print(f"Loading Model B (VADER heuristics)...")
        self.model_B = SentimentIntensityAnalyzer()
        
    def predict(self, text, force_version=None):
        cleaned_text = clean_text(text)
        if not cleaned_text:
            return {"sentiment": "Neutral", "confidence": 1.0, "scores": {"Negative":0.0, "Neutral":1.0, "Positive":0.0}, "version": "N/A"}
            
        # A/B Routing (50/50 split if not forced)
        version = force_version if force_version else random.choice(["A", "B"])
        
        if version == "A":
            # Transformers execution
            prediction = self.model_A(cleaned_text[:512])[0]
            label = prediction['label'].capitalize()
            confidence = prediction['score']
            
            if label == "Positive":
                scores = {"Negative": 1 - confidence, "Neutral": 0.0, "Positive": confidence}
            elif label == "Negative":
                scores = {"Negative": confidence, "Neutral": 0.0, "Positive": 1 - confidence}
            else:
                scores = {"Negative": 0.0, "Neutral": confidence, "Positive": 0.0}
        else:
            # VADER execution
            version = "B"
            scores_raw = self.model_B.polarity_scores(cleaned_text)
            compound = scores_raw['compound']
            
            if compound >= 0.05:
                label = "Positive"
                confidence = float(scores_raw['pos']) + 0.1
            elif compound <= -0.05:
                label = "Negative"
                confidence = float(scores_raw['neg']) + 0.1
            else:
                label = "Neutral"
                confidence = float(scores_raw['neu'])
                
            confidence = min(1.0, max(0.0, confidence)) # clamp to 0-1
            scores = {
                "Negative": float(scores_raw['neg']),
                "Neutral": float(scores_raw['neu']),
                "Positive": float(scores_raw['pos'])
            }
            
        return {
            "sentiment": label,
            "confidence": float(confidence),
            "scores": scores,
            "version": f"Model {version} {'(Transformers)' if version == 'A' else '(VADER)'}"
        }
