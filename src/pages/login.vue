<template>
  <div class="container">
    <div class="overlay">
    <div class="insidebox">
      <img src="../assets/hello.jpg" class="pfp">
      <div class="smallercontainer">
        <v-responsive>
          <v-text-field
            class="username"
            label="Username"
            color="#255b5e"
            variant="outlined"
          ></v-text-field>
        </v-responsive>    

        <v-responsive>
          <v-text-field
            class="password"
            label="Password"
            color="#FF4500"
            variant="outlined"
          ></v-text-field>
        </v-responsive>    

        <v-btn class="signup">
          <template v-slot:prepend>
            <CricketBatIcon />
          </template>
          Login
        </v-btn>
        
        <p class="text">
             Don't have an Account? 
            <router-link to="/signup" class="login-link">Signup</router-link>
          </p>
      </div>
      <div class="copyright">Copyright © 2024 Tee</div>
    </div>
  </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import CricketBatIcon from '../components/CricketBat-Icon.vue';

  const router = useRouter();

  // Function to navigate to login page
  const navigatetologin = () => {
    router.push('/signup');
  };
</script>

<style scoped>
.container {
  width: 100%;
  height: 100vh; /* Set height to viewport height */
  background-image: url('../assets/stadium.webp');
  background-size: cover;
  display: flex;
  justify-content: flex-end; /* Center horizontally */
  align-items: center; /* Center vertically */
  background-color: #d64e4a;
  z-index: -1;
}

.overlay {
  width: 100%;
  height: 100vh;
  background-image: linear-gradient(to bottom, #292929c0,#292929c0,#292929c0);
  display: flex;
  justify-content: flex-end;
  align-items: center;
  z-index: 0;
}
.insidebox {
  width: 425px;
  height: auto;
  background-color: #303030;
  border-radius: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px; /* Added padding for better spacing */
  margin-right: 1rem;
  z-index: 1000;
}

.pfp {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  margin-top: 20px; /* Adjusted margin for better alignment */
}

.username, .password {
  margin-top: 10px;
}

.smallercontainer {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 25px;
}

.v-text-field {
  width: 300px; /* Full width */
}

.signup {
  background-color: #247a65;
  color: #FFFFFF;
  margin-top: 10px;
  width: 300px;
}

.signup:hover {
  background-color: #2eb493;
  color: #FFFFFF;
}

.login-link {
  font-size: 13px;
  color: #247a65;
  margin-top: 10px;
  text-decoration: underline;
  cursor: pointer;
}
.t,.text{
    font-size: 13px;
  color: #247a65;
  margin-top: 10px;
}
.login-link:hover {
  color: #2eb493; /* Change color on hover if desired */
  text-decoration: underline;
}

.copyright {
  color: #247a65;
  margin-top: 30px;
}

</style>
