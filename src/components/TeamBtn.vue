<template>
  <div class="pa-4 text-center">
    <v-dialog v-model="dialog" max-width="600">
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn
          class="text-none font-weight-regular"
          prepend-icon="mdi-account"
          :text="text"
          variant="tonal"
          v-bind="activatorProps"
        ></v-btn>
      </template>

      <v-card prepend-icon="mdi-account" title="Add New Team">
        <v-card-text>
          <v-row dense>
            <v-col cols="12" md="4" sm="6">
              <v-text-field
                hint="example of helper text only on focus"
                label="Country"
                aria-required="Required"
                v-model="country"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-autocomplete
                :items="filteredPlayerData"
                label="Add Players"
                auto-select-first
                multiple
                v-model="selectedPlayers"
                chips
                clearable
              ></v-autocomplete>
            </v-col>
            <v-col cols="12" md="4" sm="6">
              <v-autocomplete
                :items="selectedPlayers"
                hint="add players in team first"
                label="Captain"
                auto-select-first
                v-model="captain"
                chips
              ></v-autocomplete>
            </v-col>
          </v-row>

          <small class="text-caption text-medium-emphasis">
            You can add maximum 15 players in a team
            <div>({{ selectedPlayers.length }})</div>
          </small>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>

          <v-btn
            color="primary"
            text="Save"
            variant="tonal"
            @click="handleButtonClick"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { API, UserName } from '../main';
import { makeTeam, SelectedPlayers, findChanges, updateTeam, Country,Captain , updateCaptainCountry} from './insert';

export default {
  data: () => ({
    dialog: false,
    PlayerData: [],
    selectedPlayers: SelectedPlayers ? SelectedPlayers : [],
    newSelectedPlayers: [],
    maxPlayers: 15, // Set the maximum number of players allowed
    text: '',
    captain: Captain ? Captain : null,
    country: Country ? Country : '',
    newPlayers: [],
    changed:[],
  }),
  computed: {
    filteredPlayerData() {
      // Filter PlayerData to exclude already selected players
      return this.PlayerData;
    },
  },
  watch: {
    selectedPlayers(newVal, oldVal) {
      if (newVal.length > this.maxPlayers) {
        newVal.pop();
      }

      // Check for removed players and add them back to PlayerData
      // const removedPlayers = oldVal.filter(player => !newVal.includes(player));
      // this.PlayerData.push(...removedPlayers);
    },
  },
  methods: {
    handleButtonClick() {
      if (localStorage.getItem('TeamMade') === 'no') {
        this.handleSave();
      } else {
        this.handleUpdate();
      }
    },
    showplayers(selectedPlayers) {
      console.log(selectedPlayers);
    },
    handleSave() {
      this.dialog = false;
      // for (let i = 0; i < this.selectedPlayers.length; i++) {
      //   this.newSelectedPlayers.push(this.selectedPlayers[i][0]);
      // }
      if (localStorage.getItem('TeamMade') === 'no') {
        localStorage.setItem('TeamMade', 'yes');
        makeTeam(this.selectedPlayers, this.captain, this.country);
      } else {
        console.log('Team already made');
      }
      console.log('testing123');
      console.log(this.selectedPlayers, this.captain);
      this.$emit('saveTeam', this.selectedPlayers);
      this.showplayers(this.selectedPlayers);
    },
    handleUpdate() {
      console.log('Update team');
      console.log(this.selectedPlayers, this.captain);
      this.changed = findChanges(SelectedPlayers, this.selectedPlayers);
      console.log(this.changed);
        updateTeam(this.changed);
      if(this.captain !== Captain || this.country !== Country){
        updateCaptainCountry(this.captain, this.country);
      }
    //  reload windows after2 sec
      // setTimeout(() => {
      //   window.location.reload();
      // }, 2000);
    },
  },
  mounted() {
    console.log('TeamBtn is loaded');
    localStorage.getItem('TeamMade') === 'yes'
      ? (this.text = 'Edit Team')
      : (this.text = 'Add Team');

    const requestPlayerName = async () => {
      try {
        const request = await fetch(API + '/get/player_names', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
        });
        const playerName = await request.json();
        if (playerName.status === 'ok') {
          console.log(playerName);
          console.log(playerName.players);
          console.log(this.selectedPlayers);
          this.newPlayers = playerName.players 
          for (let i = 0; i < this.newPlayers.length; i++) {
                    this.PlayerData.push(this.newPlayers[i][0]);
                }
          
        } else {
          throw new Error('Failed to POST');
        }
      } catch (e) {
        console.log(e);
        console.log('Error fetching players');
      }
    };

    requestPlayerName();
    console.log('PlayerInfo is loaded');
  },
};
</script>
