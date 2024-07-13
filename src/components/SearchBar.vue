<template>
  <div class="bar">
    <v-autocomplete
      :items="items"
      append-inner-icon="mdi-microphone"
      class="mx-auto"
      density="comfortable"
      menu-icon=""
      placeholder="Search Player"
      prepend-inner-icon="mdi-magnify"
      style="max-width: 650px;"
      theme="dark"
      textcolor="white"
      variant="solo"
      auto-select-first
      item-props
      rounded
      v-model="playerName"
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
      playerName: "",
      playerData:[],
    };
  },
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  methods: {
    showPlayer(toggle) {
      this.$emit("show", toggle, this.playerData);
    },
    search() {
      console.log("Searching for player: " + this.playerName);
      // console.log(this.items);
      if (this.items.includes(this.playerName)) {
        console.log("Player found");
        const requestPlayers = async () => {
          try {
            const request = await fetch(API + "/get/player", {
              method: "POST",
              headers: {
                "Content-Type": "application/json"
              },
              body: JSON.stringify({
                PlayerName: this.playerName
              })
            });
            const response = await request.json();
            console.log(response);
            if (response["status"] == "ok") {
              console.log(response);
              this.playerData = response["player"];
            } else {
              throw new Error("Failed to POST");
            }
          } catch (e) {
            console.log(e);
            console.log("Error fetching players");
          }
          finally {
            this.showPlayer(true);
          }
        };
        requestPlayers();
        console.log("This player is loaded" + this.playerData);
        console.log("Player found again");
      } else {
        this.showPlayer(false);
        alert("Player not found");
      }
      this.playerName = "";
      
    }
  },
  mounted() {
    console.log("SearchBar is loaded");
    console.log(this.items);
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
