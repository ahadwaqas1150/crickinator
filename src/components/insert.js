
    const API = 'http://127.0.0.1:5000'
    const UserName = localStorage.getItem("username");
    export function makeTeam(players, captain, country) {
        console.log("makeTeam is loaded")
        const insertTeam = async() => {
            try {
        const request = await fetch(API+"/insert/team", {
            method:"POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                selectedplayer: players,
                username: UserName,
                captain: captain,
                country: country
            })
        }
        );
        const playerName = await request.json();
        if(playerName["status"] == "ok") {
            console.log("Table is created");
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
insertTeam();
console.log("PlayerInfo is loaded")
}
let newSelectedPlayers = [];
export let SelectedPlayers = [];
if (localStorage.getItem('TeamMade') === 'yes') {
      // Retrieve player names from the database by sending the username
      const requestPlayerName = async () => {
        try {
          const response = await fetch(`${API}/get/playerteam`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              username: UserName
            })
          });
    
          const result = await response.json();
    
          if (result.status === "ok") {
            console.log("We are a custom team");
            console.log(result);
            newSelectedPlayers = result.team;
                for (let i = 0; i < newSelectedPlayers.length; i++) {
                    SelectedPlayers.push(newSelectedPlayers[i][0]);
                }
          } else {
            throw new Error("Failed to POST");
          }
        } catch (error) {
          console.error("Error fetching players", error);
        }
      };
    
      requestPlayerName();
    }