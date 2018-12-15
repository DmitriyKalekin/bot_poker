from flask import Flask, request, jsonify
import requests
import json
import random
from api.config import cfg
from api.connection import my_conn
from api.utils import *


app = Flask(__name__)

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
    my_cur = my_conn.cursor()  
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



    my_cur.close()
    status = 200
    return jsonify({
        "status": status,
        "error": {},
        "data": {
            "connection_token": connection_token
        },
    }), status    



