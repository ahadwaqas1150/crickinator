<template>
    <div class="bar">
      <v-autocomplete
        :items="select"
        append-inner-icon="mdi-microphone"
        class="mx-auto"
        density="comfortable"
        menu-icon=""
        placeholder="Search Teams"
        prepend-inner-icon="mdi-magnify"
        style="max-width: 650px;"
        theme="dark"
        textcolor="white"
        variant="solo"
        auto-select-first
        item-props
        rounded
        v-model="countryName"
      ></v-autocomplete>
      <v-btn @click="search"
        width="120px"
        height="50px"
        rounded="xl"
        margintop="500px"
      >Search</v-btn>
    </div>
  </template>
  
  <script>
    import { API } from "../main";
  export default {
    data() {
      return {
        countryName: "",
        playerData:[],
        select: [],
      };
    },
    methods: {
      showPlayer(toggle) {
        console.log("saim");
        this.$emit("show", toggle, this.countryName);
      },
      search() {
        this.showPlayer(true);
        console.log("Searching for team: " + this.countryName);
      }
    },
    mounted() {
      const requestOptions = async() =>{
      try {
        const request = await fetch(API+"/get/teamsName", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({})
        });
        const response = await request.json();
        console.log(response);
        if(response["status"] == "ok") {
          console.log("Teams names are here")
          console.log(response)
          this.select = response["teams"];
          console.log("This is the select")
          console.log(this.select)
        }
        else {
          response = ['no team found'];
          console.log(response)
          throw new Exception("Failed to Post")
        }
      }
      catch (error) {
        console.log('error', error);
      }
    }
    requestOptions();
    console.log("This team is loaded");
  }
  };
  </script>
  
  <style scoped>
  .bar {
    display: flex;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 600px;
    justify-content: center;
    align-content: center;
    margin: 0 auto;
  }
  </style>
  