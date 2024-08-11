"""
drop database if exists Cricketer;
-- Create the Cricketer database
CREATE DATABASE Cricketer;

-- Switch to the Cricketer database
USE Cricketer;

-- Create the PlayerData table
CREATE TABLE PlayerData(
    PlayerID INT PRIMARY KEY,
    PlayerName VARCHAR(100) NOT NULL,
    Age INT,
    PlayerRole ENUM('Batter','Bowler','AllRounder') NOT NULL,
    Subrole ENUM('Top Order','Middle Order','Finisher', 'Pacer','Spinner'),
    BattingAvg FLOAT NOT NULL,
    BattingSR FLOAT NOT NULL,
    BowlingAvg FLOAT NOT NULL,
    BowlingSR FLOAT NOT NULL,
    Economy FLOAT NOT NULL,
    Country VARCHAR(50),
    AdminCreated BOOLEAN,
    Playing11 VARCHAR(3)
);

-- Create the Article table
CREATE TABLE Article(
    ArticleName VARCHAR(255),
    ArticleLink VARCHAR(255),
    Description VARCHAR(1000)
);

-- Create the Country table
CREATE TABLE Country(
    CountryName VARCHAR(100) PRIMARY KEY,
    RecentForm VARCHAR(20)
);
--Create the users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from flask_cors import CORS
import json
import mysql.connector
from flask import request
import bcrypt
import os
import webbrowser

app = Flask(__name__)
CORS(app)
os.environ['MYSQL_USER'] = 'root'
os.environ['MYSQL_PASSWORD'] = '12345678'
print("MYSQL_USER:", os.getenv("MYSQL_USER"))
print("MYSQL_PASSWORD:", os.getenv("MYSQL_PASSWORD"))

db = mysql.connector.connect(
    host="localhost",
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    auth_plugin='mysql_native_password'
)

if db.is_connected():
    print("Connected to MySQL Server")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def send_static(path):
    print("Requested path:", path)
    links = ["","login","dashboard"]
    if path in links:
        return render_template('index.html')
    else:
        return send_from_directory('static', path)

#api to send article data to frontend
@app.route('/get/articles', methods=['POST'])
def getArticles():
    global db
    try:
        cursor = db.cursor()
        cursor.execute('USE Cricketer')
        cursor.execute('SELECT * FROM Article')
        result = cursor.fetchall()
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

    return json.dumps({'status': 'ok', 'articles': result})

#send names of players to frontend
@app.route('/get/player_names', methods=['POST'])
def getPlayers():
    global db
    try:
        cursor = db.cursor()
        cursor.execute('USE Cricketer')
        cursor.execute('SELECT PlayerName FROM PlayerData')
        result = cursor.fetchall()
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

    return json.dumps({'status': 'ok', 'players': result})

#send player data to frontend TAKING PLAYERNAME AS INPUT
@app.route('/get/player', methods=['POST'])
def getPlayerData():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data['PlayerName'][0])
        cursor.execute('USE Cricketer')
        cursor.execute('SELECT * FROM PlayerData WHERE PlayerName=%s', (data['PlayerName']))
        result = cursor.fetchone()
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

    return json.dumps({'status': 'ok', 'player': result})

#delete player from database with playerid
@app.route('/delete/player', methods=['POST'])
def deletePlayer():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data['PlayerID'])
        cursor.execute('USE Cricketer')
        cursor.execute('DELETE FROM PlayerData WHERE PlayerID=%s', (data['PlayerID'],))
        db.commit()
        return json.dumps({'status': 'ok'})
    except Exception as e:
        print('Error:', str(e))
        return json.dumps({'status': 'error', 'message': str(e)}), 500

#send team names to frontend
@app.route('/get/teamsName', methods=['POST'])
def getTeams():
    global db
    try:
        cursor = db.cursor()
        cursor.execute('USE Cricketer')
        cursor.execute('SELECT DISTINCT Country FROM PlayerData')
        result = cursor.fetchall()
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

    return json.dumps({'status': 'ok', 'teams': result})
#send players names and if they are playing 11 of a team when recieved a team name to frontend
@app.route('/get/team_players', methods=['POST'])
def getPlayersByTeam():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data['Country'][0])
        cursor.execute('USE Cricketer')
        cursor.execute('SELECT PlayerName, Playing11 FROM PlayerData WHERE Country=%s', (data['Country']))
        result = cursor.fetchall()
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

    return json.dumps({'status': 'ok', 'players': result})
#insert into database player data
@app.route('/insert/player', methods=['POST'])
def insertPlayer():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data)
        cursor.execute('USE Cricketer')
        cursor.execute('''
            INSERT INTO PlayerData(
                PlayerID,PlayerName, Age, PlayerRole, Subrole, BattingAvg, BattingSR, BowlingAvg, BowlingSR, Economy, Country, AdminCreated, Playing11
            ) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            data['PlayerID'], data['PlayerName'], data['Age'], data['PlayerRole'], data['Subrole'], 
            data['BattingAvg'], data['BattingSR'], data['BowlingAvg'], 
            data['BowlingSR'], data['Economy'], data['Country'], 
            data['AdminCreated'], data['Playing11']
        ))
        db.commit()
        return json.dumps({'status': 'ok'})
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})


#send count of players to frontend
@app.route('/get/player_count', methods=['POST'])
def getPlayerCount():
    global db
    try:
        cursor = db.cursor()
        cursor.execute('USE Cricketer')
        cursor.execute('SELECT COUNT(*) FROM PlayerData')
        result = cursor.fetchone()
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

    return json.dumps({'status': 'ok', 'count': result})
#add user into database
@app.route('/insert/user', methods=['POST'])
def insert_user():
    try:
        cursor = db.cursor()
        data = request.json
        print(data)
        
        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        cursor.execute('USE Cricketer')
        cursor.execute('''
            INSERT INTO users(
                username, email, password
            ) VALUES (%s, %s, %s)
        ''', (
            data['username'], data['email'], hashed_password.decode('utf-8')
        ))
        db.commit()
        return json.dumps({'status': 'ok'})
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

#verify user crendentials when used hash passwrods
@app.route('/verify/user', methods=['POST'])
def verifyUser():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data)
        cursor.execute('USE Cricketer')
        cursor.execute('SELECT * FROM users WHERE username=%s', (data['username'],))
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(data['password'].encode('utf-8'), result[3].encode('utf-8')):
                return json.dumps({'status': 'ok'})
            else:
                return json.dumps({'status': 'error', 'message': 'Invalid password'})
        else:
            return json.dumps({'status': 'error', 'message': 'User not found'})
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

#create a new table of users team having only player name and playing having captain written infront of a player whose name is sent from front end in database and insert players into it given an array from he front end and the name of table is the username + "team" also coming from frontend
@app.route('/insert/team', methods=['POST'])
def insertTeam():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data)
        cursor.execute('USE Cricketer')
        table_name = data['username'] + 'team'
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name}(
                ID INT AUTO_INCREMENT PRIMARY KEY,
                PlayerName VARCHAR(100) PRIMARY KEY,
                Playing VARCHAR(10),
                Country VARCHAR(50)
            )
        ''')
        for player in data['selectedplayer']:
            cursor.execute(f'''
                INSERT INTO {table_name} (
                    PlayerName, Playing, Country
                ) VALUES (%s, %s, %s)
            ''', (player, 'Member', data['country']))
        
        cursor.execute(f'''
            UPDATE {table_name}
            SET Playing = 'Captain'
            WHERE PlayerName = %s
        ''', (data['captain'],))  # Use data['captain'][0] assuming it's a list with one element

        db.commit()
        return json.dumps({'status': 'ok'})
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})
#return the team of a user from database
@app.route('/get/playerteam', methods=['POST'])
def getTeam():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data)
        cursor.execute('USE Cricketer')
        table_name = data['username'] + 'team'
        cursor.execute(f'SELECT PlayerName FROM {table_name}')
        result = cursor.fetchall()
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

    return json.dumps({'status': 'ok', 'team': result})

# Array(15)
# 0
# : 
# {index: 0, deleted: 'Abrar Ahmed', replacedBy: 'Mitchell Starc'}
# 1
# : 
# {index: 1, deleted: 'Agha Salman', replacedBy: 'Josh Hazlewood'}
# 2
# : 
# {index: 2, deleted: 'Azam Khan', replacedBy: 'Adam Zampa'}
# 3
# : 
# {index: 3, deleted: 'Babar Azam', replacedBy: 'Matthew Wade'}
# 4
# : 
# {index: 4, deleted: 'Fakhar Zaman', replacedBy: 'Josh Inglis'}
# 5
# : 
# {index: 5, deleted: 'Haris Rauf', replacedBy: 'Mitchell Marsh'}
# 6
# : 
# {index: 6, deleted: 'Hasan Ali', replacedBy: 'Marcus Stoinis'}
# 7
# : 
# {index: 7, deleted: 'Iftikhar Ahmed', replacedBy: 'Glenn Maxwell'}
# 8
# : 
# {index: 8, deleted: 'Imad Wasim', replacedBy: 'Ashton Agar'}
# 9
# : 
# {index: 9, deleted: 'Mohammad Amir', replacedBy: 'Cameron Green'}
# 10
# : 
# {index: 10, deleted: 'Mohammad Rizwan', replacedBy: 'Travis Head'}
# 11
# : 
# {index: 11, deleted: 'Naseem Shah', replacedBy: 'Tim David'}
# 12
# : 
# {index: 12, deleted: 'Saim Ayub', replacedBy: 'David Warner'}
# 13
# : 
# {index: 13, deleted: 'Shadab Khan', replacedBy: 'Nathan Ellis'}
# 14
# : 
# {index: 14, deleted: 'Shaheen Shah Afridi', replacedBy: 'Pat Cummins'}
#api to update the team of a user in database given the above array
@app.route('/update/playerteam', methods=['POST'])
def updateTeam():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data)
        cursor.execute('USE Cricketer')
        table_name = data['username'] + 'team'
        for player in data['selectedplayer']:
            cursor.execute(f'''
                UPDATE {table_name}
                SET PlayerName = %s
                WHERE PlayerName = %s
            ''', (player['replacedBy'], player['deleted']))
        
        db.commit()
        return json.dumps({'status': 'ok'})
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})
#return captain and country of a user team
@app.route('/get/captain', methods=['POST'])
def getCaptain():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data)
        cursor.execute('USE Cricketer')
        table_name = data['username'] + 'team'
        cursor.execute(f'SELECT PlayerName, Country FROM {table_name} WHERE Playing="Captain"')
        result = cursor.fetchone()
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

    return json.dumps({'status': 'ok', 'captain': result})
#update captain and country of a user team
@app.route('/update/captain', methods=['POST'])
def updateCaptain():
    global db
    try:
        cursor = db.cursor()
        data = json.loads(request.data)
        print(data)
        cursor.execute('USE Cricketer')
        table_name = data['username'] + 'team'
        cursor.execute(f'''
            UPDATE {table_name}
            SET Playing = 'Member'
            WHERE Playing = 'Captain'
        ''')
        cursor.execute(f'''
            UPDATE {table_name}
            SET Playing = 'Captain'
            WHERE PlayerName = %s
        ''', (data['captain'],))  # Use data['captain'][0] assuming it's a list with one element
        cursor.execute(f'''
            UPDATE {table_name}
            SET Country = %s
        ''', (data['country'],))
        db.commit()
        return json.dumps({'status': 'ok'})
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})

"""uSHFUIH79Ahfu7sfvhudshauioshcvuasdhfvuifdahvauihfiPHAFCU89DHFCUIASDHCVUPHASUIDVHUASVHUIADFVHDFUIAHVADFUIHV
DSBSDVBYSDVYUASGYUGAYVGYDFVBADFVBHADFHVDFUIHVUIDFVHADFUIVHDFUAHVHUAHVUAHSDVNJIASDN"""

#webbrowser.open("http://localhost:" + str(PORT), new=0, autoraise=True)
PORT = 5000
app.run(port=PORT, debug=True)
