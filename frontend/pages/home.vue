<template>
  <div class="home-page">
    <div class="hero-section">
      <h1 class="headline">Unlock Insights with our AI Sentiment Analyzer</h1>
      <p class="description">
        Instantly analyze text using state-of-the-art Deep Learning (Transformers).
        Real-time streaming, batch analysis, and CI/CD ready!
      </p>
      <button class="primary-btn" @click="$router.push('/analyzer')">
        Start Analysis
      </button>
    </div>
    
    <div class="features-grid">
      <div class="feature-card">
        <h3>Transformer Powered</h3>
        <p>Uses DistilBERT for enterprise-grade NLP performance.</p>
      </div>
      <div class="feature-card">
        <h3>Live Streaming</h3>
        <p>Connect to a WebSocket for real-time data ingestion and evaluation.</p>
      </div>
      <div class="feature-card">
        <h3>Cloud & CI/CD Ready</h3>
        <p>Dockerized and pre-configured for automated pipelines.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-page {
  text-align: center;
  animation: fadeIn 0.5s ease-in;
}

.hero-section {
  padding: 4rem 2rem;
  background: linear-gradient(135deg, #1e3a8a 0%, #312e81 100%);
  border-radius: 1rem;
  margin-bottom: 3rem;
  color: white;
}

.headline {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.description {
  font-size: 1.2rem;
  max-width: 600px;
  margin: 0 auto 2rem;
  opacity: 0.9;
}

.primary-btn {
  background-color: #3b82f6;
  color: white;
  border: none;
  padding: 1rem 2rem;
  font-size: 1.2rem;
  border-radius: 30px;
  cursor: pointer;
  transition: transform 0.2s, background-color 0.2s;
  font-weight: bold;
}

.primary-btn:hover {
  background-color: #2563eb;
  transform: translateY(-2px);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.feature-card {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.dark-theme .feature-card {
  background-color: #1e293b;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
