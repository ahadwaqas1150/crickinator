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
                    <div class="heading">
            <h1 class="display-4 text-center white--text">Add Player/Team</h1>
            <v-btn @click="showP">Add Player</v-btn>
            <v-btn  @click="showT">Add Team</v-btn>

            </div>
            <div class="table" v-if="team"> 
            <AddTeamtable :players="SelectedPlayers"/>
            <TeamBtn v-on:saveTeam="saveT"/>
        </div>
        <div class="table1" v-if="player">
            <AddPlayerCard :Information="PlayerInfo" :name="playername" ></AddPlayerCard>
            <PlayerBtn v-on:save="saveP"></PlayerBtn>
            </div>
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
    import TeamList from '@/components/TeamList.vue'; // Import TeamList component
    import PlayerTable from '@/components/PlayerTable.vue'; // Import PlayerTable component
    import AddPlayerCard from '@/components/AddPlayerCard.vue'; // Import AddPlayerCard component

    export default {
        components: {
        Main,
        PlayerInfo,
        TeamList,
        PlayerTable,
        },
        data() {
        return {
            playername: '',
            drawer: true,
            rail: true,
            team : false,
            player : false,
            teams: [
            { name: 'Pakistan', players: ['Babar Azam', 'Shaheen Afridi', 'Mohammad Rizwan', 'Azam Khan','Ahad Waqas','Ahmad Hassan Tanveer','Wajih-Us-Sama','Abdulllah Khalid'] },
            ],
            PlayerInfo: [],
            SelectedPlayers: [],
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
        methods:{
        router(){
            this.$router.push('/players')
        },
        showT(){
            this.team = true;
            this.player = false;
            this.SelectedPlayers = null;
        },
        showP(){
            this.player = !this.player;
            this.team = false;
        },
        saveP(PlayerInfo,name){
            this.PlayerInfo=PlayerInfo;
            this.playername=name;
            console.log(name);
            console.log(this.PlayerInfo);
        },
        saveT(SelectedPlayers){
            this.SelectedPlayers=SelectedPlayers;
            console.log("we are in saveT");
            console.log(this.SelectedPlayers);
        }
        }
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
        display: flex;
        justify-content: left;
        align-items: center;
        flex-wrap: wrap;
    }
    .table {
        display: flex;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 80%;
        justify-content: left;
        align-content: center;
        margin-left: 150px;
        
    }
    .table1 {
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 600px;
        justify-content: left;
        align-content: left;
        margin-left: 150px;
    }
    .img {
    justify-content: left;
    
    }
    .imgh {
    
        text-align: center;
        margin-right: 230px;
    }
    .search {
        margin-top: 80px;
        max-width: 80%;
        align-content: center;
        margin-left: 250px;
        width: 950px;
        }
        .heading {
        position: absolute;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        }
        .cardcontainer {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        width : 100svw;
        background-color: #fff;
        }
    </style>
    