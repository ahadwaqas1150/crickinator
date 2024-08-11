<template>
    <div>
      <!-- Heading -->
      <div class="heading">
        <h1 class="display-2 text-center white--text">Crickinator</h1>
        <h2 class="headline white--text">Predicting cricket match outcomes</h2>
      </div>
  
      <!-- Cards -->
      <v-container class="card-container" fluid>
        <v-row justify="center">
            <v-col v-for="item in news" :key="item" cols="12" sm="4">
            <CardComponent
              :title= item[0]
              :subtitle= item[1]
              :bodyText= item[2]
            />
          </v-col>
        </v-row>
      </v-container>
    </div>
  </template>
  
  <script>
  import CardComponent from './Card.vue'; // Import Card.vue component
  import {API} from '../main';
  
  export default {
    components: {
      CardComponent
    },
    data() {
      return {
        news: []
      }
    },
    mounted(){
      const requestNews = async() => {
      try {
        const request = await fetch(API+"/get/articles", {
          method:"POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({})
        }
        );
        const response = await request.json();
          console.log(response)
        if(response["status"] == "ok") {
          console.log(response)
          this.news = response["articles"];
        }
        else {
          throw new Exception("Failed to POST")
        }
      }
      catch(e) {
        console.log("Error fetching news");
      }
    }
    requestNews();
    console.log("This page is loaded")
    }

  };
  </script>
  
  <style scoped>
  .heading {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
  }
  
  .card-container {
    position: absolute;
    bottom: 20px;
    width: 100%;
  }
  </style>
  