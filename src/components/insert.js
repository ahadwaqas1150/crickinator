
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
export function findChanges(array1, array2) {
    let changes = [];

    // Loop through array1 to find elements that were deleted
    array1.forEach((element, index) => {
        if (!array2.includes(element)) {
            // Look for a corresponding new entry in array2
            const replacement = array2[index] !== undefined ? array2[index] : null;
            if (replacement !== null && !array1.includes(replacement)) {
                changes.push({
                    index: index,
                    deleted: element,
                    replacedBy: replacement
                });
            }
        }
    });

    // Loop through array2 to find new elements added that correspond to deletions
    array2.forEach((element, index) => {
        if (!array1.includes(element)) {
            // Look for a corresponding deleted entry in array1
            const original = array1[index] !== undefined ? array1[index] : null;
            if (original !== null && !array2.includes(original)) {
                changes.push({
                    index: index,
                    deleted: original,
                    replacedBy: element
                });
            }
        }
    });

    // Remove duplicates if any, just in case both loops detect the same change
    changes = changes.filter((change, index, self) =>
        index === self.findIndex((t) => (
            t.deleted === change.deleted && t.replacedBy === change.replacedBy
        ))
    );

    return changes;
}
// api to update user team
export function updateTeam(players) {
    console.log("updateTeam is loaded")
    const updateTeam = async() => {
        try {
        const request = await fetch(API+"/update/playerteam", {
            method:"POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                selectedplayer: players,
                username: UserName,
            })
        }
        );
        const playerName = await request.json();
        if(playerName["status"] == "ok") {
            console.log("Table is updated");
        }
        else {
            throw new Exception("Failed to POST")
        }
    }
    catch(e) {
        console.log(e);
        console.log("team was not updated");
    }
}
updateTeam();
console.log("PlayerInfo is loaded")
}
// get captain and country
export let Captain = "";
export let Country = "";
    const getCaptainCountry = async() => {
        try {
        const request = await fetch(API+"/get/captain", {
            method:"POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: UserName,
            })
        }
        );
        const playerName = await request.json();
        if(playerName["status"] == "ok") {
            console.log("Captain and country fetched");
            console.log(playerName);
            Captain = playerName.captain[0];
            Country = playerName.captain[1];
            console.log(Captain , Country);
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
getCaptainCountry();
console.log("PlayerInfo is loaded")
// update captain and country
export function updateCaptainCountry(captain, country) {
    console.log("updateCaptainCountry is loaded")
    const updateCaptainCountry = async() => {
        try {
        const request = await fetch(API+"/update/captain", {
            method:"POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: UserName,
                captain: captain,
                country: country
            })
        }
        );
        const playerName = await request.json();
        if(playerName["status"] == "ok") {
            console.log("Captain and country updated");
        }
        else {
            throw new Exception("Failed to POST")
        }
    }
    catch(e) {
        console.log(e);
        console.log("Captain and country was not updated");
    }
}
updateCaptainCountry();
console.log("PlayerInfo is loaded")
}