<template>
  <div>
    <!-- Navigation Drawer -->
    <v-navigation-drawer v-model="drawer" :rail="rail" permanent @click="rail = !rail">
      <!-- Drawer content -->
      <v-list-item prepend-avatar="https://randomuser.me/api/portraits/men/85.jpg" :title=userName nav>
        <template v-slot:append>
          <v-btn icon variant="text" @click.stop="rail = !rail">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
        </template>
      </v-list-item>

      <v-divider></v-divider>

      <!-- Customized Navigation Links -->
      <v-list dense nav>
        <v-list-item @click="this.$router.push('/welcome')" prepend-icon="mdi-home-city">
          <slot name="home">Home</slot>
        </v-list-item>
        <v-list-item @click="this.$router.push('/players')" prepend-icon="mdi-account">
          <slot name="players">Players</slot>
        </v-list-item>
        <v-list-item @click="this.$router.push('/test')" prepend-icon="mdi-account-group-outline">
          <slot name="test">Teams</slot>
        </v-list-item>
        <v-list-item @click="this.$router.push('/Insert')" prepend-icon="mdi-account-multiple-plus">
          <slot name="Insert">Add</slot>
        </v-list-item>
        <v-list-item @click="this.$router.push('/predict')" prepend-icon="mdi-plus-minus-variant">
          <slot name="predict">Calculate</slot>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Main content area -->
    <v-app-bar :elevation="8">
      <template v-slot:prepend>
        <v-btn icon @click="rail = !rail">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </template>
      <v-app-bar-title>Cricket Prediction</v-app-bar-title>
    </v-app-bar>

    <!-- Background image with overlay -->
    <div class="background">
      <v-container fluid>
        <v-layout justify-center align-center>
          <v-img
            src="@/assets/stadium.webp"
            alt="Background Image"
            :width="viewportWidth"
            :height="viewportHeight"
            cover
          >
            <!-- Overlay -->
            <div class="overlay">
              <div class="overlay2">

                <div class="half black">
                  <v-autocomplete
                  label="Autocomplete"
                  :items="filteredItems1"
                  v-model="selected1"
                  variant="solo-inverted"
                  width="50%"
                  ></v-autocomplete>
                  <v-img
                  width="300px"  
                  height="auto" 
                  src="@/assets/file.png"
                  ></v-img>
                </div>
                <div class="half white">
                  <v-autocomplete
                  label="Autocomplete"
                  :items="filteredItems2"
                  v-model="selected2"
                  variant="solo-inverted"
                  width="50%"
                  ></v-autocomplete>
                  <v-img
                  width="300px"  
                  height="auto" 
                  src="@/assets/file.png"
                  ></v-img>
                </div>
                
              </div>
              <!-- <div class="graph">
                <Graph />
              </div> -->

              </div>
          </v-img>
        </v-layout>
      </v-container>
    </div>
  </div>
</template>

<script>
import {getUserName} from '../main';
export default {
  data() {
    return {
      drawer: true,
      rail: true,
      items: ['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming'],
      selected1: null,
      selected2: null,
      userName: getUserName(),
    };
  },
  computed: {
    viewportWidth() {
      return window.innerWidth;
    },
    viewportHeight() {
      return window.innerHeight;
    },
    filteredItems1() {
      if (this.selected2) {
        return this.items.filter(item => item !== this.selected2);
      }
      return this.items;
    },
    filteredItems2() {
      if (this.selected1) {
        return this.items.filter(item => item !== this.selected1);
      }
      return this.items;
    },
  },
};
</script>

<style scoped>
.background {
  position: relative;
}
.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
}
.overlay2 {
  display: flex;
  /* flex-direction: row;
  justify-content: center;
  align-items: center;
  background: rgba(255, 255, 255, 0.7);
  margin-left: 230px;
  padding-top: 90px; */
}
.half {
  width: 50%;
  height: 70%;
  /* display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center; 
  background: rgba(255, 255, 255, 0.7); */
  margin-left: 230px;
  padding-top: 90px; 
}
.graph {
  position: absolute;
  width: 50%;
  height: 100px;
  margin-left: 200px;
}
</style>
