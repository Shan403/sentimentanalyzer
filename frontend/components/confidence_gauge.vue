<template>
  <div class="gauge-container">
    <div class="gauge">
      <svg viewBox="0 0 100 50" class="gauge-svg">
        <path class="gauge-bg" d="M 10 50 A 40 40 0 0 1 90 50" fill="none" stroke-width="10" stroke-linecap="round" />
        <path class="gauge-fill" :stroke-dasharray="dashArray" d="M 10 50 A 40 40 0 0 1 90 50" fill="none" stroke-width="10" stroke-linecap="round" />
      </svg>
      <div class="gauge-text">
        <span class="percent">{{ (confidence * 100).toFixed(0) }}%</span>
        <span class="label">Confidence</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    confidence: {
      type: Number,
      required: true,
      default: 0
    }
  },
  computed: {
    dashArray() {
      const circumference = 125.66;
      const fillAmount = (this.confidence * circumference);
      return `${fillAmount}, ${circumference}`;
    }
  }
}
</script>

<style scoped>
.gauge-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.gauge {
  position: relative;
  width: 200px;
  height: 100px;
}

.gauge-svg {
  width: 100%;
  height: 100%;
}

.gauge-bg {
  stroke: #e2e8f0;
}

.dark-theme .gauge-bg {
  stroke: #334155;
}

.gauge-fill {
  stroke: #3b82f6;
  transition: stroke-dasharray 0.8s ease-out;
}

.gauge-text {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  display: flex;
  flex-direction: column;
}

.percent {
  font-size: 2rem;
  font-weight: bold;
  line-height: 1;
}

.label {
  font-size: 0.8rem;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 1px;
}
</style>
