<template>
  <div class="pa-4 text-center">
    <v-dialog v-model="dialog" max-width="600">
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn
          class="text-none font-weight-regular"
          prepend-icon="mdi-account"
          text="New Player"
          variant="tonal"
          v-bind="activatorProps"
          @click="newbox"
        ></v-btn>
      </template>

      <v-card prepend-icon="mdi-account" title="Add New Player">
        <v-card-text>
          <v-row dense>
            <v-col cols="12" md="4" sm="6">
              <v-text-field label="Name*" required v-model="name"></v-text-field>
            </v-col>

            <v-col cols="12" md="4" sm="6">
              <v-text-field
                hint="example of helper text only on focus"
                label="Batting Avg"
                aria-required="Required"
                required
                v-model="battingAvg"
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="4" sm="6">
              <v-text-field
                hint="example of persistent helper text"
                label="BattingSr"
                required
                v-model="battingSr"
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="4" sm="6">
              <v-text-field
                label="Bowling Avg"
                required
                v-model="bowlingAvg"
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="4" sm="6">
              <v-text-field
                label="BowlingSr"
                required
                v-model="bowlingSr"
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="4" sm="6">
              <v-text-field
                label="Economy"
                required
                v-model="economy"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="4" sm="6">
              <v-text-field
                label="Country"
                required
                v-model="country"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="4" sm="6">
              <v-text-field
                label="Age"
                required
                v-model="age"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-select
                :items="[
                  'Batter',
                  'Bowler',
                  'AllRounder',
                ]"
                label="Player Role"
                required
                v-model="role"
              ></v-select>
            </v-col>

            <v-col cols="12" sm="6">
              <v-select
                :items="[
                  'Top Order',
                  'Middle Order',
                  'Finisher',
                  'Pacer',
                  'Spinner'
                ]"
                label="SubRole"
                required
                v-model="subRole"
              ></v-select>
            </v-col>
          </v-row>

          <small class="text-caption text-medium-emphasis">{{ name }} , </small>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>
          <v-btn color="primary" text="Save" variant="tonal" @click="updatePlayerInfo"></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { API } from "../main";
export default {
  data() {
    return {
      dialog: false,
      PlayerID: '',
      name: '',
      battingAvg: '',
      battingSr: '',
      bowlingAvg: '',
      bowlingSr: '',
      economy: '',
      country: '',
      role: '',
      subRole: '',
      age: '',
      PlayerInfo: []
    };
  },
  methods: {
    updatePlayerInfo() {
      // Update PlayerInfo with current form data
      this.PlayerInfo = [
        { title: 'PlayerRole', value: this.role },
        { title: 'Subrole', value: this.subRole },
        { title: 'BattingAvg', value: this.battingAvg },
        { title: 'BattingSR', value: this.battingSr },
        { title: 'BowlingAvg', value: this.bowlingAvg },
        { title: 'BowlingSR', value: this.bowlingSr },
        { title: 'Economy', value: this.economy },
        { title: 'Country', value: this.country },
        { title: 'Age', value: this.age }
      ];
      this.save();
      this.dialog = false; // Close dialog
    },
    async save() {
      this.$emit('save', this.PlayerInfo, this.name);
      console.log('Player info saved:', this.PlayerInfo);
      try {
        const request = await fetch(API + "/insert/player", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            PlayerID: this.PlayerID,
            PlayerName: this.name,
            PlayerRole: this.role,
            Subrole: this.subRole,
            BattingAvg: this.battingAvg,
            BattingSR: this.battingSr,
            BowlingAvg: this.bowlingAvg,
            BowlingSR: this.bowlingSr,
            Economy: this.economy,
            Country: this.country,
            Age: this.age,
            AdminCreated: false,
            Playing11: "no"
          })
        });
        const response = await request.json();
        console.log(response);
        if (response["status"] === "ok") {
          console.log(response);
          this.playerData = response["data"];
        } else {
          throw new Error("Failed to POST");
        }
      } catch (e) {
        console.log(e);
        console.log("Error fetching players");
      } 
    },
    newbox() {
      this.name = '';
      this.battingAvg = '';
      this.battingSr = '';
      this.bowlingAvg = '';
      this.bowlingSr = '';
      this.economy = '';
      this.country = '';
      this.role = '';
      this.subRole = '';
      this.age = '';
    }
  },
  mounted() {
    // get player count from backend
    const requestPlayers = async () => {
      try {
        const request = await fetch(API + "/get/player_count", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({})
        });
        const response = await request.json();
        console.log(response);
        if (response["status"] === "ok") {
          console.log(response);
          this.PlayerID = response["count"][0] + 1;
          console.log(this.PlayerID);
        } else {
          throw new Error("Failed to POST");
        }
      } catch (e) {
        console.log(e);
        console.log("Error fetching players");
      }
    };
    requestPlayers();
    console.log("This wajih is loaded");
  }
};
</script>
