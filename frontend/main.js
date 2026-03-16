import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './app.vue'
import Home from './pages/home.vue'
import Analyzer from './pages/analyzer.vue'
import Batch from './pages/batch.vue'
import Insights from './pages/insights.vue'
import About from './pages/about.vue'
import Stream from './pages/stream.vue'
import './index.css'

const routes = [
  { path: '/', component: Home },
  { path: '/analyzer', component: Analyzer },
  { path: '/batch', component: Batch },
  { path: '/stream', component: Stream },
  { path: '/insights', component: Insights },
  { path: '/about', component: About },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

const app = createApp(App)
app.use(router)
app.mount('#app')
