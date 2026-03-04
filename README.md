# AI Sentiment Analyzer 🚀

A professional, full-stack AI application that predicts the sentiment of text using Machine Learning.

## ✨ Features
- **Real-time Prediction**: Instantly detect if text is Positive, Neutral, or Negative.
- **Batch Analysis**: Analyze multiple lines of text simultaneously.
- **Visual Analytics**: Interactive confidence gauges and probability distribution charts.
- **Modern UI**: Multi-page design with smooth transitions and **Light/Dark mode** support.
- **FastAPI Backend**: High-performance Python API for ML inference.

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI, scikit-learn, pandas, numpy.
- **Frontend**: Vite, Vue 3 (Antigravity architecture), CSS Grid/Flexbox.
- **ML Model**: Logistic Regression with TF-IDF Vectorization.

## 🚀 Getting Started

### 1. Clone & Setup Backend
```bash
# Clone the repository
git clone <your-repo-url>
cd sentiment_analyzer

# Install dependencies
pip install -r requirements.txt

# Train the model (optional if .pkl exists)
python backend/train_model.py

# Run backend
python -m uvicorn backend.main:app --reload
```

### 2. Setup Frontend
```bash
cd frontend
npm install
npm run dev
```
The frontend of this project is built using the Antigravity framework, where UI files use the .ag extension. These files define the layout, pages, and components of the web interface. The .ag files can be edited in VS Code or any other IDE, but they are executed using the Antigravity runtime, not directly from the IDE.
To run the project, first install the required dependencies using pip install antigravity fastapi uvicorn pandas numpy scikit-learn matplotlib seaborn. Then start the backend server with uvicorn main:app --reload. After that, run the frontend using antigravity run app.ag. Once both services are running, open the local server in your browser to access the sentiment analyzer web application.

## 📊 Model Information
The model was trained on a dataset of ~241k comments using TF-IDF feature extraction and a Logistic Regression classifier, achieving high accuracy for sentiment classification.

sentiment_analyzer/
├── backend/
│   ├── main.py
│   ├── sentiment_predictor.py
│   └── train_model.py
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── app.ag
│   ├── index.css
│   ├── index.html
│   ├── main.js
│   ├── package.json
│   └── vite.config.js
├── models/
│   └── sentiment_model.pkl
├── .gitignore
├── README.md
├── requirements.txt
└── sentiment_data.csv




