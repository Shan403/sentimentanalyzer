import pandas as pd
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from transformers import pipeline

# Instead of training basic ML, this script evaluates the Deep Learning model on existing data!
# Simulating a monitoring/data-drift check by evaluating predictions against labels.

def evaluate_deep_learning_model(data_path='../sentiment_data.csv'):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if data_path.startswith('../'):
        data_path = os.path.join(base_dir, data_path.replace('../', ''))
        
    print(f"Loading data for Evaluation / Drift Check from: {data_path}")
    if not os.path.exists(data_path):
        print("Dataset not found. Cannot evaluate drift.")
        return
        
    df = pd.read_csv(data_path)
    
    # Try with a small subset to prevent hours of local inference
    sample_size = min(200, len(df))
    df = df.sample(n=sample_size, random_state=42)
    
    print(f"Evaluating DistilBERT model on a sample of {sample_size} rows...")
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    nlp_pipeline = pipeline("sentiment-analysis", model=model_name)
    
    y_true = []
    y_pred = []
    
    for _, row in df.iterrows():
        text = str(row['comment'])[:512]
        true_label = row['sentiment'] # 0: negative, 1: neutral, 2: positive
        
        # DL Prediction
        res = nlp_pipeline(text)[0]
        label = res['label'].upper()
        
        if label == "POSITIVE":
            pred_label = 2
        elif label == "NEGATIVE":
            pred_label = 0
        else:
            pred_label = 1
            
        y_true.append(true_label)
        y_pred.append(pred_label)
        
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    rec = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    
    print("\n--- MODEL MONITORING & PERFORMANCE ---")
    print(f"Accuracy:  {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall:    {rec:.4f}")
    print(f"F1 Score:  {f1:.4f}")
    
    if acc < 0.8:
        print("\n[WARNING] Data Drift Detected: Accuracy has fallen below acceptable baseline! Model fine-tuning required.")
    else:
        print("\n[OK] Model performance is stable against this slice of data.")

if __name__ == "__main__":
    evaluate_deep_learning_model()
