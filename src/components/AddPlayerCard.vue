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
          {{ name }}
        </v-card-subtitle>
        <v-card-subtitle>
          T-20 opener
        </v-card-subtitle>
        <v-card-actions>
        <v-btn
            color="orange-lighten-2"
            text="More Info"
            @click="array()"
        ></v-btn>
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
            </div>
                    </v-card-text>
                </div>
            </v-expand-transition>
        </v-card>
    </template>
    <script>
    export default {
        data: () => ({
        show: false,
        }),
        props: {
        Information: {
            type: Array,
        },
        name: {
            type: String,
        },
      },
        methods: { 
        array() {
        console.log(this.Information);
        console.log(this.name);
        }
      }
};

</script>
<style scoped>
    .flex-content {
      flex: 1; /* Take the remaining space */
  overflow-y: auto;
    }
    .scroll {
      max-height: 300px;
      overflow-y: scroll;
    }
    .scroll::-webkit-scrollbar {
  width: 14px; /* Width of the scrollbar */
  border-radius: 12px;
}

.scroll::-webkit-scrollbar-thumb {
  background-color: #2e3130ec; /* Color of the scrollbar thumb */
  border-radius: 12px; /* Roundness of the scrollbar thumb */
  border: 2px solid #037b8800; /* Padding around the scrollbar thumb */
}

.scroll::-webkit-scrollbar-thumb:hover {
  background-color: #ffffff; /* Color of the scrollbar thumb when hovered */
}

.scroll::-webkit-scrollbar-track {
  background: #1c1c1c03; /* Color of the scrollbar track */
  border-radius: 12px;
}

</style>