<template>
  <v-card
      class="mx-auto"
      width="500px"
      overflowed
  >
      <v-card-title>
          Player info
      </v-card-title>
      <v-card-subtitle>
        {{ items[1] }}
      </v-card-subtitle>
      <v-card-subtitle>
        Playing: {{ items[12] }}
      </v-card-subtitle>
      <v-card-actions>
      
      <v-spacer></v-spacer>
      <v-btn
          :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
          @click="show = !show"
      ></v-btn>
      </v-card-actions>
      <v-expand-transition>
          <div v-show="show">
              <v-divider></v-divider>
              <v-card-text>
                <div class="scroll">
                  <v-expansion-panels class="flex-content"  v-for="(item, index) in Information" :key="index">
                    <v-expansion-panel
                      :title="item.title"
                      :text="item.value"
                    >
                  </v-expansion-panel>
                </v-expansion-panels>
                <v-btn
          color="orange-lighten-2"
          text="Delete player"
          width="100%"
          v-if="items[11] === 1"
          disabled
          @click="array()"
      ></v-btn>
                <v-btn
          color="orange-lighten-2"
          text="Delete player"
          width="100%"
          v-if="items[11] === 0"
          @click="array()"
      ></v-btn>
                </div>
              </v-card-text>
          </div>
      </v-expand-transition>
  </v-card>
</template>

<script>
 import { API } from "../main";
export default {
  data: () => ({
    show: false,
    name:'Talal',
    img: "",
  }),
  props: {
    items: {
      type: Array,
      required: true
    },
    Information: {
      type: Array,
      required: true
    }
  },
  computed: {
    filteredItems() {
  return this.items.filter((item, index) => index !== 0 && index !== 11);
},
  },
  watch: {
    items: {
      handler() {
        console.log("Items changed");
      },
      deep: true
    }
  },
  methods: {
    array() {
      console.log("In array");
      const requestPlayers = async () => {
  try {
    const request = await fetch(API + "/delete/player", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        PlayerID: this.items[0]
      })
    });

    const response = await request.json();
    console.log('Response:', response);

    if (response.status === "ok") {
      console.log("Player deleted successfully");
      window.location.reload()
    } else {
      throw new Error(`Failed to POST: ${response.message}`);
    }
  } catch (e) {
    console.error(e);
    console.log("Error fetching players");
  }
};

        requestPlayers();
        console.log("In array 2");
        }

  },
mounted() {
    console.log("playercard is loaded");
    console.log(this.items);
    console.log(this.Information);
  }
};
</script>

<style scoped>
.flex-content {
  flex: 1;
  overflow-y: auto;
}
.scroll {
  max-height: 300px;
  overflow-y: scroll;
}
.scroll::-webkit-scrollbar {
  width: 14px;
  border-radius: 12px;
}
.scroll::-webkit-scrollbar-thumb {
  background-color: #2e3130ec;
  border-radius: 12px;
  border: 2px solid #037b8800;
}
.scroll::-webkit-scrollbar-thumb:hover {
  background-color: #ffffff;
}
.scroll::-webkit-scrollbar-track {
  background: #1c1c1c03;
  border-radius: 12px;
}
</style>
