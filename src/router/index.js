import { createRouter, createWebHistory } from 'vue-router'
import Index from '../pages/index.vue'
import Players from '../pages/players.vue'
import Test from '../pages/test.vue'
import Insert from '../pages/Insert.vue'
import Predict from '../pages/predict.vue'
import signup from '@/pages/signup.vue'
import login from '@/pages/login.vue'
import Welcome from '@/pages/welcome.vue'




const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index
  },
  {
    path: '/welcome',
    name: 'Welcome',
    component: Welcome
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
  },
  {
    path: '/signup',
    name: 'signup',
    component: signup
  },
  {
    path: '/login',
    name: 'login',
    component: login
  }

  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
