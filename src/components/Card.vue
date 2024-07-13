<!-- CardComponent.vue -->
<template>
    <v-card class="mx-auto my-8" elevation="16" max-width="344" @mouseover="hoverCard(true)" @mouseleave="hoverCard(false)">
      <v-card-item>
        <v-card-title>{{ title }}</v-card-title>
        <!-- <v-card-subtitle>{{ title }}</v-card-subtitle> -->
      </v-card-item>
      <v-card-text>
        {{ bodyText }}
      </v-card-text>
      <v-card-actions>
    <v-btn @click="loadPage()">More info</v-btn>
  </v-card-actions>
    </v-card>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      subtitle: String,
      bodyText: String
    },
    methods: {
      hoverCard(isHovered) {
        if (isHovered) {
          this.$emit('hovered', this.title);
      }
    },
    loadPage() {
      window.open(this.subtitle, '_blank');
    }
  }
}
  </script>
  
  <style scoped>
  /* Add scoped styles if needed */
  </style>
  