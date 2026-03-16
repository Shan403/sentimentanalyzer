<template>
  <div class="batch-page">
    <h2>Batch Sentiment Analysis</h2>
    <p class="subtitle">Upload a text file or enter multiple lines to analyze them all at once.</p>

    <div class="input-card">
      <textarea 
        v-model="batchText" 
        placeholder="Enter multiple lines of text here (one comment per line)..."
        class="batch-input"
        rows="10"
      ></textarea>
      <div class="actions">
        <button @click="analyzeBatch" class="analyze-btn" :disabled="isAnalyzing || !batchText.trim()">
          {{ isAnalyzing ? 'Processing Batch...' : 'Analyze Batch' }}
        </button>
        <button @click="clearBatch" class="clear-btn">Clear</button>
      </div>
    </div>

    <div v-if="results.length > 0" class="results-container">
      <div class="summary-card">
        <h3>Batch Summary</h3>
        <div class="summary-stats">
          <div class="stat">
            <span class="label">Total</span>
            <span class="value">{{ results.length }}</span>
          </div>
          <div class="stat positive">
            <span class="label">Positive</span>
            <span class="value">{{ summary.positive }}</span>
          </div>
          <div class="stat neutral">
            <span class="label">Neutral</span>
            <span class="value">{{ summary.neutral }}</span>
          </div>
          <div class="stat negative">
            <span class="label">Negative</span>
            <span class="value">{{ summary.negative }}</span>
          </div>
        </div>
      </div>

      <div class="results-table-container">
        <table class="results-table">
          <thead>
            <tr>
              <th>Text Snippet</th>
              <th>Sentiment</th>
              <th>Confidence</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(res, index) in results" :key="index">
              <td class="snippet">{{ res.text.substring(0, 60) }}{{ res.text.length > 60 ? '...' : '' }}</td>
              <td>
                <span class="badge" :class="res.sentiment.toLowerCase()">{{ res.sentiment }}</span>
              </td>
              <td class="confidence">{{ (res.confidence * 100).toFixed(1) }}%</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      batchText: '',
      isAnalyzing: false,
      results: []
    }
  },
  computed: {
    summary() {
      const counts = { positive: 0, neutral: 0, negative: 0 };
      this.results.forEach(r => {
        counts[r.sentiment.toLowerCase()]++;
      });
      return counts;
    }
  },
  methods: {
    async analyzeBatch() {
      this.isAnalyzing = true;
      this.results = [];
      const lines = this.batchText.split('\n').filter(line => line.trim() !== '');
      
      try {
        for (const line of lines) {
          const response = await fetch('https://sentiment-analyzer-backend-u9jw.onrender.com/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_text: line })
          });
          const data = await response.json();
          this.results.push({
            text: line,
            sentiment: data.sentiment,
            confidence: data.confidence
          });
        }
      } catch (error) {
        console.error("Error in batch analysis", error);
      } finally {
        this.isAnalyzing = false;
      }
    },
    clearBatch() {
      this.batchText = '';
      this.results = [];
    }
  }
}
</script>

<style scoped>
.batch-page {
  animation: fadeIn 0.4s ease-in;
}

.subtitle {
  margin-bottom: 2rem;
  opacity: 0.7;
}

.input-card {
  background-color: var(--card-bg, #ffffff);
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  margin-bottom: 2rem;
}

.dark-theme .input-card {
  background-color: #1e293b;
  --card-bg: #1e293b;
}

.batch-input {
  width: 100%;
  padding: 1rem;
  border-radius: 0.5rem;
  border: 1px solid #e2e8f0;
  background-color: #f8fafc;
  color: inherit;
  font-family: inherit;
  font-size: 1rem;
  resize: vertical;
  margin-bottom: 1rem;
}

.dark-theme .batch-input {
  background-color: #0f172a;
  border-color: #334155;
}

.actions {
  display: flex;
  gap: 1rem;
}

.analyze-btn {
  background-color: #3b82f6;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: bold;
  cursor: pointer;
}

.clear-btn {
  background-color: transparent;
  border: 1px solid #e2e8f0;
  color: inherit;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
}

.results-container {
  margin-top: 2rem;
}

.summary-card {
  background-color: #3b82f6;
  color: white;
  padding: 1.5rem;
  border-radius: 1rem;
  margin-bottom: 2rem;
}

.summary-stats {
  display: flex;
  justify-content: space-around;
  margin-top: 1rem;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat .label { font-size: 0.8rem; opacity: 0.9; }
.stat .value { font-size: 1.5rem; font-weight: bold; }

.results-table-container {
  background-color: var(--card-bg, #ffffff);
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.dark-theme .results-table-container {
  background-color: #1e293b;
}

.results-table {
  width: 100%;
  border-collapse: collapse;
}

.results-table th, .results-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
}

.dark-theme .results-table th, .dark-theme .results-table td {
  border-bottom-color: #334155;
}

.badge {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.8rem;
  font-weight: bold;
  text-transform: uppercase;
}

.badge.positive { background-color: #dcfce7; color: #166534; }
.badge.neutral { background-color: #f1f5f9; color: #475569; }
.badge.negative { background-color: #fee2e2; color: #991b1b; }

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>
