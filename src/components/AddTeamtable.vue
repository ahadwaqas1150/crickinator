<template>
    <div class="tab">
      <v-table width="500px">
        <thead>
          <tr>
            <th class="text-left">Name</th>
            <th class="text-left">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(player, index) in players" :key="index">
            <td><v-btn :ripple="false">{{ player }}</v-btn></td>
            <td><div @click="rout" class="value">Player info</div></td>
          </tr>
        </tbody>
      </v-table>
    </div>
  </template>
  
  <script>
import router from '@/router';

  export default {
    props: {
      players: {
        type: Array,
        required: true,
      },
    },
    methods:{
    rout(){
      this.$router.push('/players')
    }
    }
  };
  </script>
  
  <style scoped>
  .tab {
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 600px;
    justify-content: left;
    align-content: left;
    /* Enable overflow for the entire container */
  }
  
  .v-table tbody {
    max-height: 350px; /* Set max height for the table body */
    overflow-y: auto; /* Enable vertical scrolling */
    display: block; /* Display block to apply overflow */
  }
  
  .v-table thead, .v-table tbody tr {
    display: table;
    width: 100%;
    table-layout: fixed; /* Fix table layout for both head and body */
  }
  
  .value:hover {
    background-color: #10e9ac72;
    transform: scale(1.03);
  }
  </style>
  