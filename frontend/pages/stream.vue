<template>
  <div class="stream-page">
    <h2>Live Sentiment Stream</h2>
    <p class="subtitle">Connects via WebSocket to analyze text streams in real-time.</p>

    <div class="stream-controls">
      <button :class="['connect-btn', { connected: isConnected }]" @click="toggleConnection">
        {{ isConnected ? 'Disconnect Stream' : 'Connect to Stream' }}
      </button>
      <span class="status-indicator">
        Status: <strong>{{ isConnected ? 'Live 🟢' : 'Offline 🔴' }}</strong>
      </span>
    </div>

    <div class="input-card" v-if="isConnected">
      <input 
        v-model="liveInput" 
        @keyup.enter="sendLiveText"
        placeholder="Type a message and press Enter..."
        class="live-input"
      />
      <button @click="sendLiveText" class="send-btn">Send</button>
    </div>

    <div class="stream-log">
      <h3>Stream Log</h3>
      <div class="log-container">
        <div v-if="logs.length === 0" class="empty-log">No messages yet. Connect and send text.</div>
        <div v-for="(log, idx) in logs" :key="idx" class="log-item">
          <div class="log-text">{{ log.text }}</div>
          <div class="log-result">
            <span class="badge" :class="log.sentiment?.toLowerCase() || 'unknown'">{{ log.sentiment || 'Waiting...' }}</span>
            <span v-if="log.confidence" class="conf">{{ (log.confidence * 100).toFixed(1) }}%</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isConnected: false,
      socket: null,
      liveInput: '',
      logs: []
    }
  },
  methods: {
    toggleConnection() {
      if (this.isConnected) {
        if (this.socket) {
          this.socket.close();
        }
        this.isConnected = false;
      } else {
        this.socket = new WebSocket('wss://sentiment-analyzer-backend-u9jw.onrender.com/ws/stream');
        
        this.socket.onopen = () => {
          this.isConnected = true;
          this.logs.unshift({ text: 'System: Stream Connected', sentiment: 'NEUTRAL', confidence: 1.0 });
        };
        
        this.socket.onmessage = (event) => {
          const data = JSON.parse(event.data);
          // find the waiting log and update it
          const pendingLog = this.logs.find(l => l.text === data.original_text && !l.sentiment);
          if (pendingLog) {
            pendingLog.sentiment = data.sentiment;
            pendingLog.confidence = data.confidence;
          } else {
            this.logs.unshift({
               text: data.original_text || 'Unknown stream data',
               sentiment: data.sentiment,
               confidence: data.confidence
            });
          }
        };
        
        this.socket.onclose = () => {
          this.isConnected = false;
          this.logs.unshift({ text: 'System: Stream Disconnected', sentiment: 'NEUTRAL', confidence: 1.0 });
        };
      }
    },
    sendLiveText() {
      if (!this.liveInput.trim() || !this.isConnected) return;
      
      this.logs.unshift({ text: this.liveInput, sentiment: null, confidence: null });
      this.socket.send(this.liveInput);
      this.liveInput = '';
    }
  },
  beforeUnmount() {
    if (this.socket) {
      this.socket.close();
    }
  }
}
</script>

<style scoped>
.stream-page { animation: fadeIn 0.4s ease-in; }
.subtitle { margin-bottom: 2rem; opacity: 0.7; }
.stream-controls { display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; }
.connect-btn { background-color: #3b82f6; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.5rem; cursor: pointer; font-weight: bold; }
.connect-btn.connected { background-color: #ef4444; }
.status-indicator { font-size: 0.9rem; }
.input-card { display: flex; gap: 0.5rem; margin-bottom: 2rem; }
.live-input { flex: 1; padding: 0.75rem; border-radius: 0.5rem; border: 1px solid #e2e8f0; background-color: #ffffff; color: inherit; }
.dark-theme .live-input { background-color: #1e293b; border-color: #334155; }
.send-btn { background-color: #10b981; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; cursor: pointer; font-weight: bold; }
.stream-log { background-color: #ffffff; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.dark-theme .stream-log { background-color: #1e293b; }
.log-container { display: flex; flex-direction: column; gap: 0.5rem; max-height: 400px; overflow-y: auto; margin-top: 1rem; }
.log-item { display: flex; justify-content: space-between; align-items: center; padding: 0.75rem; border-bottom: 1px solid #e2e8f0; }
.dark-theme .log-item { border-bottom-color: #334155; }
.empty-log { color: #94a3b8; font-style: italic; }
.badge { padding: 0.2rem 0.6rem; border-radius: 1rem; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; }
.badge.positive { background-color: #dcfce7; color: #166534; }
.badge.neutral { background-color: #f1f5f9; color: #475569; }
.badge.negative { background-color: #fee2e2; color: #991b1b; }
.conf { font-size: 0.8rem; margin-left: 0.5rem; opacity: 0.8; }
</style>
