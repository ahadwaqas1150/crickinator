<template>
    <div class="player-info">
      <div class="heading">
        <h1 class="display-4 text-center white--text">PLAYER INFO</h1>
      </div>
      <div class="search">  
        <SearchBar @show="show" :items="PlayerData"></SearchBar>
      </div>
      <div v-if="showPlayer"  class="card-container">
        <v-row justify="center" align-content="center">
          <v-col cols="12" sm="8">
            <div class="player">
              <PlayerCard 
              :items="sendData"
              :Information="Information"
              />
            </div>
          </v-col>
          <v-col class="img" cols="12" sm="4">
            <v-img
              width="300px"  
              height="auto" 
              :src="sendData[13]"
            ></v-img>
          </v-col>
        </v-row>
      </div>
    </div>
  </template>
  
  <script>
  import PlayerCard from '@/components/PlayerCard.vue';
  import SearchBar from '@/components/SearchBar.vue'; // Assuming SearchBar component path
  import {API} from '../main';
  
  export default {
    data(){
      return{
        showPlayer: false,
        PlayerData: [],
        sendData: [],
        img: 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_320,q_50/lsci/db/PICTURES/CMS/319700/319794.png',
        Information: []
      }
    },
    components: {
      PlayerCard,
      SearchBar
    },
methods:{
    show(toggle,playerData){
      console.log("hello")
    console.log(playerData)
      this.showPlayer = toggle;
      this.sendData = playerData;
      this.Information = [
        { title: 'PlayerRole', value: this.sendData[3] },
        { title: 'Subrole', value: this.sendData[4] },
        { title: 'BattingAvg', value: this.sendData[5] },
        { title: 'BattingSR', value: this.sendData[6] },
        { title: 'BowlingAvg', value: this.sendData[7] },
        { title: 'BowlingSR', value: this.sendData[8] },
        { title: 'Economy', value: this.sendData[9] },
        { title: 'Country', value:this.sendData[10] },
        { title: 'Age', value: this.sendData[2] }
      ];
      // PlayerInfo = response;
    }
  },
  mounted() {
    const requestPlayerName = async() => {
      try {
        const request = await fetch(API+"/get/player_names", {
          method:"POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({})
        }
        );
        const playerName = await request.json();
        if(playerName["status"] == "ok") {
          console.log(playerName)
          this.PlayerData = playerName.players;
        }
        else {
          throw new Exception("Failed to POST")
        }
      }
      catch(e) {
        console.log(e);
        console.log("Error fetching players");
      }
    }
    requestPlayerName();
    console.log("PlayerInfo is loaded")
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
  
  .search {
    margin-top: 80px;
    max-width: 80%;
    align-content: center;
    margin-left: 150px;
  }
  
  .player {
    width: 500px;
    margin-left: 200px;
    padding: 50px;
    
  }
  
  .player :hover {
    background-color: #05aa7895;
  }
  
  </style>
  