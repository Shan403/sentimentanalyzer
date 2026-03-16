<template>
  <div class="about-page">
    <h2>About AI Sentiment Analyzer Pro</h2>
    
    <div class="content-card">
      <h3>How the Deep Learning Model Works</h3>
      <p>
        We have upgraded our engine to use <strong>HuggingFace Transformers (DistilBERT)</strong>. Instead of basic word-counting (TF-IDF) and Logistic Regression, we now use a neural network that understands the context and semantics of words in a sentence.
      </p>
      <ul>
        <li><strong>Tokenization:</strong> Text is converted into sub-word tokens compatible with BERT.</li>
        <li><strong>Inference:</strong> The transformer evaluates the sequence and outputs logits.</li>
        <li><strong>Prediction:</strong> We apply a softmax function to return probabilities for Positive and Negative sentiment.</li>
      </ul>
    </div>

    <div class="content-card">
      <h3>Enterprise Architecture</h3>
      <ul>
        <li><strong>CI/CD Pipeline:</strong> Fully automated tests and builds using GitHub Actions.</li>
        <li><strong>Dockerized:</strong> Ready to deploy anywhere using standard containers.</li>
        <li><strong>Real-time Streams:</strong> WebSocket integration for continuous data pipelines.</li>
        <li><strong>Monitoring:</strong> Integrated Prometheus metrics for measuring latency and drift.</li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.about-page {
  max-width: 800px;
  margin: 0 auto;
  animation: fadeIn 0.4s ease-in;
}

.content-card {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 1rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.dark-theme .content-card {
  background-color: #1e293b;
}

h3 {
  color: #3b82f6;
  margin-top: 0;
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 0.5rem;
}

.dark-theme h3 {
  border-bottom-color: #334155;
}

ul {
  padding-left: 1.5rem;
  line-height: 1.6;
}

li {
  margin-bottom: 0.5rem;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>
