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
              color="#FF4500"
              variant="outlined"
              v-model="username"
            ></v-text-field>
          </v-responsive>    
  
          <v-responsive>
            <v-text-field
              class="email"
              label="Email"
              color="#FF4500"
              variant="outlined"
              v-model="email"
              type="email"
            ></v-text-field>
          </v-responsive>  
  
          <v-responsive>
            <v-text-field
              class="password"
              label="Password"
              color="#FF4500"
              variant="outlined"
              v-model="password"
              type="password"
            ></v-text-field>
          </v-responsive>    
  
          <v-btn class="signup" @click="signup()">
            <template v-slot:prepend>
              <CricketBatIcon />
            </template>
            Signup
          </v-btn>
  
          <!-- Use router-link for navigation -->
          <p class="text">
            Already have an Account? 
            <router-link to="/login" class="login-link">Login</router-link>
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
    import { ref } from 'vue';
    import { API } from '../main';

    let username = ref('');
    let email = ref('');
    let password = ref('');
    const router = useRouter();
  
    // Function to navigate to login page
    const navigatetologin = () => {
      router.push('/login');
    };
    const signup = () => {
      console.log("Signup clicked");
      //send data to backend
      console.log(username.value, email.value, password.value);
      const requestNews = async() => {
        try {
          const response = await fetch(API+"/insert/user", {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              username: username.value,
              email: email.value,
              password: password.value
            })
          });
          const data = await response.json();
          console.log(data);
          // Redirect to login page
          if(data["status"] == "ok") {
            navigatetologin();
          }
        } catch (error) {
          console.error(error);
        }
      };
      requestNews();

      // Navigate to login page
      
    };
  </script>
  
  <style scoped>
  .container {
    width: 100%;
    height: 100vh; /* Set height to viewport height */
    background-image: url('../assets/stadium.webp');
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    background-size: cover;
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
  }
  
  .pfp {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin-top: 20px; /* Adjusted margin for better alignment */
  }
  
  .username, .email, .password {
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
  
  .text {
    font-size: 13px;
    color: #247a65;
    margin-top: 7px;
  }
  
  .login-link {
    text-decoration: underline;
    cursor: pointer;
    color: #247a65;
  }
  
  .login-link:hover {
    color: #2eb493; /* Change color on hover if desired */
  }
    
  .copyright {
    color: #247a65;
    margin-top: 30px;
  }
  </style>
  