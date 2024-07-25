    import {API, UserName} from "../main";
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