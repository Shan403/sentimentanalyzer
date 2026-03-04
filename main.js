import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './app.ag'
import Home from './pages/home.ag'
import Analyzer from './pages/analyzer.ag'
import Insights from './pages/insights.ag'
import About from './pages/about.ag'
import Batch from './pages/batch.ag'
import './index.css'

const routes = [
    { path: '/', component: Home },
    { path: '/analyzer', component: Analyzer },
    { path: '/batch', component: Batch },
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
