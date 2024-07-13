<template>
  <div>
    <!-- Navigation Drawer -->
    <v-navigation-drawer
      v-model="drawer"
      :rail="rail"
      permanent
      @click="rail = !rail"
    >
      <!-- Drawer content -->
      <v-list-item
        prepend-avatar="https://randomuser.me/api/portraits/men/85.jpg"
        title="John Leider"
        nav
      >
        <template v-slot:append>
          <v-btn
            icon
            variant="text"
            @click.stop="rail = !rail"
          >
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
        </template>
      </v-list-item>
      
      <v-divider></v-divider>

      <!-- Customized Navigation Links -->
      <v-list dense nav>
        <v-list-item @click=" this.$router.push('/')" prepend-icon="mdi-home-city">
                    <slot name="home">Home</slot>
                </v-list-item>
                <v-list-item @click=" this.$router.push('/players')"  prepend-icon="mdi-account">
                    <slot name="players">Players</slot>
                </v-list-item>
                <v-list-item @click=" this.$router.push('/test')" prepend-icon="mdi-account-group-outline">
                    <slot name="test">Teams</slot>
                </v-list-item>
                <v-list-item @click=" this.$router.push('/Insert')" prepend-icon="mdi-account-multiple-plus">
                    <slot name="Insert">Add</slot>
                </v-list-item>
                <v-list-item @click="this.$router.push('/predict')" prepend-icon="mdi-plus-minus-variant">
                    <slot name="predict">Calculate</slot>
                </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Main content area -->
    <v-app-bar :elevation="8">
      <!-- AppBar content -->
      <template v-slot:prepend>
        <v-btn icon @click="rail = !rail">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </template>
      <v-app-bar-title>Cricket Prediction</v-app-bar-title>
    </v-app-bar>

    <!-- Background image with overlay -->
    <div class="background">
      <!-- Content within background area -->
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
              <PlayerInfo />
            </div>
          </v-img>
        </v-layout>
      </v-container>
    </div>
  </div>
</template>

<script>
import Main from '@/components/Main.vue'; // Import Main.vue component
import PlayerInfo from '@/components/PlayerInfo.vue'; // Import new PlayerInfo component
import {API} from '../main';
import { Exception } from 'sass';
export default {
  components: {
    Main,
    PlayerInfo
  },
  data() {
    return {
      drawer: true,
      rail: true,
    };
  },
  computed: {
    viewportWidth() {
      return window.innerWidth;
    },
    viewportHeight() {
      return window.innerHeight;
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
  background: rgba(0, 0, 0, 0.7); /* Overlay color */
}
</style>
