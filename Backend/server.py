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
"""

from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from flask_cors import CORS
import json
import mysql.connector
from flask import request
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

"""uSHFUIH79Ahfu7sfvhudshauioshcvuasdhfvuifdahvauihfiPHAFCU89DHFCUIASDHCVUPHASUIDVHUASVHUIADFVHDFUIAHVADFUIHV
DSBSDVBYSDVYUASGYUGAYVGYDFVBADFVBHADFHVDFUIHVUIDFVHADFUIVHDFUAHVHUAHVUAHSDVNJIASDN"""

#webbrowser.open("http://localhost:" + str(PORT), new=0, autoraise=True)
PORT = 5000
app.run(port=PORT, debug=True)
