<template>
    <v-navigation-drawer :value="drawer" :rail="rail" permanent @click="closeRail">
      <v-list-item
        prepend-avatar="https://randomuser.me/api/portraits/men/85.jpg"
        title="John Leider"
        nav
      >
        <template v-slot:append>
          <v-btn icon variant="text" @click.stop="closeRail">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
        </template>
      </v-list-item>
  
      <v-divider></v-divider>
  
      <v-list dense nav>
        <v-list-item prepend-icon="mdi-home-city" title="Home" @click="navigate('index')"></v-list-item>
        <v-list-item prepend-icon="mdi-account" title="Players" @click="navigate('players')"></v-list-item>
        <v-list-item prepend-icon="mdi-account-group-outline" title="Teams" @click="navigate('teams')"></v-list-item>
      </v-list>
    </v-navigation-drawer>
  </template>
  
  <script>
  export default {
    name: 'NavigationDrawer',
    props: {
      drawer: Boolean,
      rail: Boolean
    },
    methods: {
      closeRail() {
        this.$emit('update:rail', false);
      },
      navigate(route) {
        // Emit a custom event to handle navigation based on the clicked item
        this.$emit('navigate', route);
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add scoped styles if needed */
  </style>
  