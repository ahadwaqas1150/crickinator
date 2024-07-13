/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

export const API = 'http://127.0.0.1:5000'
 
// Composables
import { createApp } from 'vue'
import "./styles/global.css"

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
