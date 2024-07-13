import { createRouter, createWebHistory } from 'vue-router'
import Index from '../pages/index.vue'
import Players from '../pages/players.vue'
import Test from '../pages/test.vue'
import Insert from '../pages/Insert.vue'
import Predict from '../pages/predict.vue'



const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index
  },
  {
    path: '/players',
    name: 'Players',
    component: Players
  },
  {
    path: '/test',
    name: 'Test',
    component: Test
  },
  {
    path: '/Insert',
    name: 'Insert',
    component: Insert
  },
  {
    path: '/predict',
    name: 'Predict',
    component: Predict
  }

  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
