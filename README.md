# AI Sentiment Analyzer Pro

An enterprise-grade, full-stack AI application designed to analyze the sentiment of text in real-time. Upgraded to use **Deep Learning Transformers**, A/B Testing, WebSockets, and Cloud CI/CD.

## 🌟 Enterprise Features

*   **Deep Learning (Transformers)**: Replaced basic ML techniques with HuggingFace's `distilbert-base-uncased-finetuned-sst-2` for state-of-the-art context and semantic understanding.
*   **A/B Testing routing**: Live traffic is routed simultaneously between Model A (DistilBERT) and Model B (VADER Heuristics) to compare edge-case accuracy on the fly.
*   **Real-time Streaming**: Connect via WebSockets (`ws://`) to stream simulated live social media text directly into the inference engine with ZERO overhead.
*   **Model Monitoring & Drift Detection**: Integrated Prometheus metrics for continuous MLOps and a batch data-drift evaluator to automatically flag accuracy regressions. 
*   **Modern Frontend framework**: Built on standard Vue SFCs (`.vue`), Vite, and styled cohesively.
*   **Cloud Ready**: Full `Dockerfile` and automated GitHub Action CI/CD pipelines. Config maps included for fast `Render` backend and `Vercel` HTTP static deployment.

## 📂 Project Architecture

```text
sentiment_analyzer/
├── backend/
│   ├── main.py                # FastAPI server (WebSockets, Prometheus, A/B Engine)
│   ├── sentiment_predictor.py  # Model inference loader (Transformer + VADER)
│   └── train_model.py          # MLOps Drift Evaluation Script
├── frontend/
│   ├── components/            # Vue UI components (Charts, Gauges)
│   ├── pages/                 # Multi-page Vue views (Stream, Analyze, Insights)
│   ├── app.vue                # Main application shell
│   ├── main.js                # Frontend entry & Routing
│   ├── index.html             # HTML template
│   ├── package.json           # Frontend dependencies
│   ├── vercel.json            # Deployment config for frontend
│   └── vite.config.js         # Build configuration
├── Dockerfile                 # Container image steps
├── render.yaml                # Deployment config for backend
├── .github/workflows          # CI/CD Action definitions
├── README.md                  # Project documentation
└── requirements.txt           # Python backend dependencies
```

## 🚀 Getting Started Locally

### 1. Start the Backend Server
Requires Python 3.10+. This will automatically download the HuggingFace `distilbert` model on the first run.
```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```
*API is accessible at http://127.0.0.1:8000*
*Prometheus Metrics are accessible at http://127.0.0.1:8000/metrics*

### 2. Monitor Data Drift
To run a batch analytics test mimicking an MLOps drift warning system:
```bash
python backend/train_model.py
```

### 3. Start the Frontend Dashboard
Open a new terminal session.
```bash
cd frontend
npm install
npm run dev
```
*Dashboard is accessible at http://localhost:5173*
