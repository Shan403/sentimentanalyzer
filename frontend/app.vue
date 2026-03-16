<template>
  <div class="app-layout" :class="{ 'dark-theme': isDarkTheme }">
    <nav class="navbar">
      <div class="logo">AI Sentiment Analyzer</div>
      <div class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/analyzer">Analyzer</router-link>
        <router-link to="/batch">Batch Analysis</router-link>
        <router-link to="/stream">Live Stream</router-link>
        <router-link to="/insights">Metrics</router-link>
        <router-link to="/about">About</router-link>
        <button @click="toggleTheme" class="theme-toggle">
          {{ isDarkTheme ? '☀️ Light' : '🌙 Dark' }}
        </button>
      </div>
    </nav>
    <main class="content-container">
      <router-view></router-view>
    </main>
    <footer class="footer">
      <p>&copy; AI Sentiment Analyzer Pro. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isDarkTheme: true
    };
  },
  methods: {
    toggleTheme() {
      this.isDarkTheme = !this.isDarkTheme;
    }
  }
}
</script>

<style>
.app-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: 'Inter', sans-serif;
  transition: background-color 0.3s, color 0.3s;
  background-color: #f8fafc;
  color: #1e293b;
}

.dark-theme {
  background-color: #0f172a;
  color: #f1f5f9;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #ffffff;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  transition: background-color 0.3s;
}

.dark-theme .navbar {
  background-color: #1e293b;
  box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.logo {
  font-weight: 800;
  font-size: 1.5rem;
  color: #3b82f6;
  letter-spacing: -0.5px;
}

.nav-links {
  display: flex;
  align-items: center;
}

.nav-links a {
  margin: 0 1rem;
  text-decoration: none;
  color: inherit;
  font-weight: 500;
  transition: color 0.2s;
  font-size: 0.95rem;
}

.nav-links a.router-link-active {
  color: #3b82f6;
  font-weight: 700;
}

.nav-links a:hover {
  color: #3b82f6;
}

.theme-toggle {
  background-color: #f1f5f9;
  border: 1px solid #e2e8f0;
  color: #475569;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  cursor: pointer;
  margin-left: 1rem;
  font-weight: 600;
  transition: all 0.2s;
}

.dark-theme .theme-toggle {
  background-color: #334155;
  border-color: #475569;
  color: #f1f5f9;
}

.theme-toggle:hover {
  background-color: #e2e8f0;
}

.dark-theme .theme-toggle:hover {
  background-color: #475569;
}

.content-container {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.footer {
  text-align: center;
  padding: 1rem;
  font-size: 0.9rem;
  opacity: 0.8;
}
</style>
