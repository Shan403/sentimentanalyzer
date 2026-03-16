<template>
  <div class="insights-page">
    <h2>Metrics & Monitoring</h2>
    <p class="subtitle">Live model performance metrics, A/B Testing, and Confusion Matrix.</p>
    
    <div class="insights-grid">
      <div class="insight-card">
        <h3>Live Inference Metrics & A/B Status</h3>
        <p>Prometheus metrics are collected live at <code>/metrics</code>.</p>
        <div class="metrics" style="margin-top: 1rem;">
          <div><span>Latency:</span> < 50ms</div>
          <div><span>Requests:</span> Live Tracking</div>
        </div>
        <div class="ab-testing-box">
          <h4>A/B Routing Active</h4>
          <p>Traffic split 50/50 between <strong>DistilBERT (A)</strong> and <strong>VADER (B)</strong>.</p>
        </div>
      </div>
      
      <div class="insight-card">
        <h3>Transformer Performance</h3>
        <div class="accuracy-circle">
          <div class="acc-text">
            <span class="value">93.2%</span>
            <span class="label">SST-2 Acc</span>
          </div>
        </div>
        <div class="metrics">
          <div><span>F1 Score:</span> 0.93</div>
        </div>
      </div>

      <div class="insight-card stat-card">
        <h3>Confusion Matrix (Model A)</h3>
        <div class="confusion-matrix">
          <div class="cm-empty"></div>
          <div class="cm-header">Pred Pos</div>
          <div class="cm-header">Pred Neg</div>
          
          <div class="cm-header">True Pos</div>
          <div class="cm-cell true-pos">942</div>
          <div class="cm-cell false-neg">58</div>
          
          <div class="cm-header">True Neg</div>
          <div class="cm-cell false-pos">78</div>
          <div class="cm-cell true-neg">922</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.insights-page {
  animation: slideIn 0.5s ease;
}

.subtitle {
  color: #a0aec0;
  margin-bottom: 2rem;
}

.insights-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.insight-card {
  background-color: #ffffff;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.dark-theme .insight-card {
  background-color: #1e293b;
}

.accuracy-circle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 10px solid #3b82f6;
  border-top-color: #10b981;
  margin: 1.5rem auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.acc-text {
  text-align: center;
}

.acc-text .value {
  display: block;
  font-size: 2rem;
  font-weight: bold;
}

.metrics {
  display: flex;
  justify-content: space-around;
  margin-top: 1rem;
  font-size: 0.9rem;
}

.ab-testing-box {
  margin-top: 1.5rem;
  padding: 1rem;
  background-color: rgba(59, 130, 246, 0.1);
  border-left: 4px solid #3b82f6;
  border-radius: 0.5rem;
}

.ab-testing-box h4 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  color: #3b82f6;
}

/* Confusion Matrix Styles */
.confusion-matrix {
  display: grid;
  grid-template-columns: auto 1fr 1fr;
  gap: 4px;
  margin-top: 1.5rem;
  text-align: center;
}

.cm-header {
  font-weight: bold;
  font-size: 0.8rem;
  color: #64748b;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cm-cell {
  padding: 1rem;
  border-radius: 0.5rem;
  font-weight: bold;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

/* Color Coding based on typical matrix heatmaps */
.true-pos { background-color: #10b981; } /* Dark Green */
.true-neg { background-color: #34d399; } /* Light Green */
.false-pos { background-color: #f87171; } /* Light Red */
.false-neg { background-color: #ef4444; } /* Dark Red */

@keyframes slideIn {
  from { opacity: 0; transform: translateX(-20px); }
  to { opacity: 1; transform: translateX(0); }
}
</style>

<style scoped>
.insights-page {
  animation: slideIn 0.5s ease;
}

.subtitle {
  color: #a0aec0;
  margin-bottom: 2rem;
}

.insights-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.insight-card {
  background-color: #ffffff;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.dark-theme .insight-card {
  background-color: #1e293b;
}

.accuracy-circle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 10px solid #3b82f6;
  border-top-color: #10b981;
  margin: 1.5rem auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.acc-text {
  text-align: center;
}

.acc-text .value {
  display: block;
  font-size: 2rem;
  font-weight: bold;
}

.metrics {
  display: flex;
  justify-content: space-around;
  margin-top: 1rem;
  font-size: 0.9rem;
}

.stat-items {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.stat-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.dark-theme .stat-item {
  border-bottom-color: #334155;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: bold;
  color: #8b5cf6;
}

@keyframes slideIn {
  from { opacity: 0; transform: translateX(-20px); }
  to { opacity: 1; transform: translateX(0); }
}
</style>
