from flask import Flask, jsonify, request
import game
import random
import uuid

app = Flask(__name__)
core = game.Core()


# S'assure de l'authenticité des messages en générant un token à chaque message

players = {}

def _generate_token(player):
    token = uuid.uuid4()
    players[player.id] = token
    return token.hex

def _check_token(id, hex_token):
    print("players:", players)
    print(players.)
    return (id in players.keys and players.get(id).hex == hex_token)


# Permet de générer l'identifiant du joueur
@app.route('/login', methods = ['POST'])
def login():
    player = game.Player(core)
    return jsonify(
        id = player.id,
        token = _generate_token(player)
    )

# Envoie la citation et la suggestion d'auteurs
@app.route('/quotes', methods = ['POST'])
def quotes():
    id = request.form['id']
    token = request.form['token']

    if _check_token(id, token):
        player = game.Player.players[id]

        return jsonify(

            token = _generate_token(player)
        )