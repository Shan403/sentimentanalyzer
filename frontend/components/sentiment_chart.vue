<template>
  <div class="chart-container">
    <div class="bar-row" v-for="(val, key) in scores" :key="key">
      <div class="label">{{ key }}</div>
      <div class="bar-track">
        <div class="bar-fill" :class="key.toLowerCase()" :style="{ width: `${val * 100}%` }"></div>
      </div>
      <div class="value">{{ (val * 100).toFixed(1) }}%</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    scores: {
      type: Object,
      required: true,
      default: () => ({ Positive: 0, Negative: 0 })
    }
  }
}
</script>

<style scoped>
.chart-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem 0;
}

.bar-row {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.label {
  width: 80px;
  text-align: right;
  font-weight: 500;
  font-size: 0.9rem;
  text-transform: capitalize;
}

.bar-track {
  flex: 1;
  height: 12px;
  background-color: #e2e8f0;
  border-radius: 6px;
  overflow: hidden;
}

.dark-theme .bar-track {
  background-color: #334155;
}

.bar-fill {
  height: 100%;
  border-radius: 6px;
  transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.bar-fill.positive { background-color: #10b981; }
.bar-fill.neutral { background-color: #9ca3af; }
.bar-fill.negative { background-color: #ef4444; }

.value {
  width: 50px;
  text-align: right;
  font-size: 0.9rem;
  font-variant-numeric: tabular-nums;
}
</style>
