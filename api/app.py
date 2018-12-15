from flask import Flask, request, jsonify
import requests
import json
import random
from api.config import cfg
from api.connection import my_conn
from api.utils import *
from random import random


app = Flask(__name__)
bot = {

}

# --------------------------------------------------------- ADMIN ---------------------------------------------
@app.route('/off', methods=['POST', 'GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

@app.errorhandler(404)
def page_not_found(e):
    status = 404
    return jsonify({
        "status": status,
        "error": {"description": "Not found"},
        "data": {},
    }), status

@app.errorhandler(500)
def internal_server_error(e):
    status = 500
    return jsonify({
        "status": status,
        "error": {"description": "Server error"},
        "data": {},
    }), status


# --------------------------------------------------------- GAME ---------------------------------------------
@app.route('/', methods=['POST', 'GET'])
def index():
    status = 200
    return jsonify({
        "status": status,
        "error": {},
        "data": {},
    }), status



@app.route('/register', methods=['POST', 'GET'])
def register():
    my_cur = my_conn.cursor()  

    name = request.args.get('name', type = str)
    pwd = request.args.get('pwd', type = str)

    if not name:
        status = 400
        return jsonify({
            "status": status,
            "error": {"description": "required param NAME"},
            "data": {},
        }), status   

    if not pwd:
        status = 400
        return jsonify({
            "status": status,
            "error": {"description": "required param PWD"},
            "data": {},
        }), status          

    my_cur.execute(f"""
    INSERT IGNORE INTO players SET
    name = '{name}',
    pwd = '{pwd}',
    connection_token = MD5('{name}'); 
    """)

    my_cur.execute(f"""
    SELECT 
    player_id, 	name, 	pwd, 	connection_token
    FROM players WHERE name='{name}' AND pwd='{pwd}'
    LIMIT 1;
    """)
    row = my_cur.fetchall()

    if len(row) == 0:
        status = 401
        return jsonify({
            "status": status,
            "error": {"description": "Username and password incorrect"},
            "data": {},
        }), status           

    player_id, name, pwd, connection_token = row[0]
    my_cur.close()        
    

    status = 200
    return jsonify({
        "status": status,
        "error": {},
        "data": {
            "player_id": player_id,
            "name": name,
            "connection_token": connection_token
        },
    }), status    



@app.route('/play', methods=['POST', 'GET'])
def play():
    # my_cur = my_conn.cursor()  
    connection_token = request.args.get('connection_token', type = str)

    if not check_token(connection_token):
        status = 401
        return jsonify({
            "status": status,
            "error": {"description": "Connection_token required. Use endpoint /register"},
            "data": {
                "connection_token": connection_token
            },
        }), status   

    if connection_token not in  bot:
        bot[connection_token] = {
            "game_id": 123123,
            "round": 0,
            "started_balance": 100000,
            "bet_size": 5,
            "distribution": "134719123", 
  
            "player": {
                    "name": "player",
                    "current_balance": 1000,
                    "cards": random(),
                "status": {
                    "code": 0,
                    "description": "ready"
                }                 
            },
            "opponent": {
                "name": "bot8888",
                "current_balance": 1000,
                "cards": random(),
                "status": {
                    "code": 0,
                    "description": "ready"
                } 
            }
        }



    # my_cur.close()
    status = 200
    return jsonify({
        "status": status,
        "error": {},
        "data": bot[connection_token],
    }), status    


@app.route('/play/move', methods=['POST', 'GET'])
def play_move():
    # my_cur = my_conn.cursor()  
    connection_token = request.args.get('connection_token', type = str)
    action = request.args.get('action', type = str)

    if not check_token(connection_token):
        status = 401
        return jsonify({
            "status": status,
            "error": {"description": "Connection_token required. Use endpoint /register"},
            "data": {
                "connection_token": connection_token
            },
        }), status   
    
    if action not in ["fold", "bet"]:
        status = 400
        return jsonify({
            "status": status,
            "error": {"description": "Action must be fold/bet"},
            "data": {},
        }), status    

    bot_action = "bet" if bot[connection_token]["opponent"]["cards"] > 0.75 else "fold"

    if bot_action=="fold" and action=="fold":
        bot[connection_token]["player"]["current_balance"] -= 1
        bot[connection_token]["opponent"]["current_balance"] -= 1

    if bot_action=="bet" and action=="fold":
        bot[connection_token]["player"]["current_balance"] -= 1
        bot[connection_token]["opponent"]["current_balance"] += 1        

    if bot_action=="fold" and action=="bet":
        bot[connection_token]["player"]["current_balance"] += 1
        bot[connection_token]["opponent"]["current_balance"] -= 1      

    if bot_action=="bet" and action=="bet":
        if  bot[connection_token]["player"]["cards"] > bot[connection_token]["opponent"]["cards"]:
            bot[connection_token]["player"]["current_balance"] += 6
            bot[connection_token]["opponent"]["current_balance"] -= 6 
        else:
            bot[connection_token]["player"]["current_balance"] -= 6
            bot[connection_token]["opponent"]["current_balance"] += 6 
         

    # my_cur.close()
    status = 200
    return jsonify({
        "status": status,
        "error": {},
        "data": bot[connection_token],
    }), status  


