# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies - use CPU-only torch to keep image small
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download model at build time to cache the deep learning model (DistilBERT)
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')"

# Copy remaining code
COPY . .

# Expose ports for FastAPI backend
EXPOSE 10000

# Run FastAPI using uvicorn on Render's expected port
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "10000"]
