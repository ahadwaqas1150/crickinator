<template>
    <div class="pa-4 text-center">
      <v-dialog v-model="dialog" max-width="600">
        <template v-slot:activator="{ props: activatorProps }">
          <v-btn
            class="text-none font-weight-regular"
            prepend-icon="mdi-account"
            text="Edit team"
            variant="tonal"
            v-bind="activatorProps"
          ></v-btn>
        </template>
  
        <v-card prepend-icon="mdi-account" title="Add New Team">
          <v-card-text>
            <v-row dense>
              <v-col cols="12" md="4" sm="6">
                <v-text-field label="Name*" required></v-text-field>
              </v-col>
  
              <v-col cols="12" md="4" sm="6">
                <v-text-field
                  hint="example of helper text only on focus"
                  label="Country"
                  aria-required="Required"
                ></v-text-field>
              </v-col>
  
              <v-col cols="12" md="4" sm="6">
                <v-text-field
                  hint="example of persistent helper text"
                  label="Captain"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-autocomplete
                  :items="[
                    'Babar Azam',
                    'Shaheen Afridi',
                    'Mohammad Rizwan',
                    'Azam Khan',
                    'Ahad Waqas',
                    'Ahmad Hassan Tanveer',
                    'Wajih-Us-Sama',
                    'Abdulllah Khalid',
                    'kohli',
                    'Rohit Sharma',
                    'MS Dhoni',
                    'williamson',
                    'kumar singhakara',
                    'sachin tendulkar',
                    'malinga',
                    'muralitharan',
                    'sangakara',
                  ]"
                  label="Add Players"
                  auto-select-first
                  multiple
                  v-model="selectedPlayers"
                  chips
                ></v-autocomplete>
              </v-col>
            </v-row>
  
            <small class="text-caption text-medium-emphasis"
              >*indicates required field</small
            >
          </v-card-text>
  
          <v-divider></v-divider>
  
          <v-card-actions>
            <v-spacer></v-spacer>
  
            <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>
  
            <v-btn
              color="primary"
              text="Save"
              variant="tonal"
              @click="handleSave"
            ></v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </template>
  
  <script>
  export default {
    data: () => ({
      dialog: false,
      selectedPlayers: [],
      maxPlayers: 15, // Set the maximum number of players allowed
    }),
    watch: {
      selectedPlayers(newVal) {
        if (newVal.length > this.maxPlayers) {
          newVal.shift();
        }
      },
    },
    methods: {
      showplayers(selectedPlayers) {
        console.log(selectedPlayers);
      },
      handleSave() {
        this.dialog = false;
        this.$emit('saveTeam', this.selectedPlayers);
        this.showplayers(this.selectedPlayers);
      },
    },
  };
  </script>
  