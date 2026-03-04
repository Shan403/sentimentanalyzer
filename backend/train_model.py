import pandas as pd
import numpy as np
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import os

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def train_and_save_model(data_path=None, model_dir=None):
    # Determine absolute paths relative to the project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if data_path is None:
        data_path = os.path.join(base_dir, 'sentiment_data.csv')
    if model_dir is None:
        model_dir = os.path.join(base_dir, 'models')
        
    print(f"Using data path: {data_path}")
    print(f"Using model directory: {model_dir}")
    if not os.path.exists(data_path):
        print("Data file not found. Creating a small dummy dataset for demonstration...")
        data = {
            'index': range(300),
            'comment': ['This is wonderful!'] * 100 + ['This is okay.'] * 100 + ['This is terrible.'] * 100,
            'sentiment': [2] * 100 + [1] * 100 + [0] * 100
        }
        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(data_path), exist_ok=True)
        df.to_csv(data_path, index=False)
    else:
        df = pd.read_csv(data_path)
    
    if 'comment' not in df.columns or 'sentiment' not in df.columns:
        raise ValueError("Dataset must contain 'comment' and 'sentiment' columns.")
        
    print("Preprocessing text...")
    df['cleaned_comment'] = df['comment'].apply(clean_text)
    
    vectorizer = TfidfVectorizer(max_features=10000)
    X = vectorizer.fit_transform(df['cleaned_comment'])
    y = df['sentiment']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        
    print("Saving model and vectorizer...")
    with open(os.path.join(model_dir, 'sentiment_model.pkl'), 'wb') as f:
        pickle.dump({'model': model, 'vectorizer': vectorizer}, f)
        
    print("Done!")

if __name__ == "__main__":
    train_and_save_model()
