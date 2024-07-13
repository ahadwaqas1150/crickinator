<template>
    <div class="teams" v-for="team in teams" :key="team.name">
      <v-fade-transition>
        <v-card class="pa-4" width="300px" flat>
          <v-card-title>{{ team.name }}</v-card-title>
          <v-list>
            <v-list-item v-for="player in team.players" :key="player">
              <v-list-item-content>
                <v-list-item-title>{{ player }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card>
      </v-fade-transition>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      teams: {
        type: Array,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .teams {
    margin: 20px;
  }
  .teams:hover {
    transform: scale(1.01);
  }
  .teams v-list-item-title:hover {
    transform: scale(1.0);
    background-color: #565656cc;
  }
  </style>
  