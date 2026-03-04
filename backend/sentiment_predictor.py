import pickle
import os
import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

class SentimentPredictor:
    def __init__(self, model_path=None):
        if model_path is None:
            # Fallback to default relative path from this file
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            model_path = os.path.join(base_dir, 'models', 'sentiment_model.pkl')
            
        self.model = None
        self.vectorizer = None
        if os.path.exists(model_path):
            with open(model_path, 'rb') as f:
                data = pickle.load(f)
                self.model = data['model']
                self.vectorizer = data['vectorizer']
        else:
            print(f"Model path {model_path} does not exist. Please train the model first.")
                
        self.label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}

    def predict(self, text):
        if not self.model or not self.vectorizer:
            return {"sentiment": "Unknown", "confidence": 0.0, "scores": {}}
            
        cleaned_text = clean_text(text)
        if not cleaned_text:
            return {"sentiment": "Neutral", "confidence": 1.0, "scores": {"Negative":0.0, "Neutral":1.0, "Positive":0.0}}
            
        features = self.vectorizer.transform([cleaned_text])
        prediction = self.model.predict(features)[0]
        probabilities = self.model.predict_proba(features)[0]
        
        confidence = probabilities[list(self.model.classes_).index(prediction)]
        
        scores = {}
        for idx, cp in enumerate(self.model.classes_):
            label_name = self.label_map.get(cp, "Unknown")
            scores[label_name] = float(probabilities[idx])
            
        return {
            "sentiment": self.label_map.get(prediction, "Unknown"),
            "confidence": float(confidence),
            "scores": scores
        }
