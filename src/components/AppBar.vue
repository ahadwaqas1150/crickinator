<template>
    <v-app-bar :elevation="8">
      <template v-slot:prepend>
        <v-btn icon @click="$emit('toggleDrawer')">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </template>
      <v-app-bar-title>Cricket Prediction</v-app-bar-title>
    </v-app-bar>
  </template>
  
  <script>
  export default {
    name: 'AppBar'
  };
  </script>
  
  <style scoped>
  /* Add scoped styles if needed */
  </style>
  