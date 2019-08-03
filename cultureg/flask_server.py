from . import game
from flask import Flask, jsonify, request
import random
import uuid


app = Flask(__name__)
core = game.Core()


# Génère un token et l'attribue au joueur
def _generate_token(player):
    token = uuid.uuid4()
    player.token = token
    return token.hex

# Permet de récupérer un joueur en fonction de son id si son token est le bon
def _get_player(id, hex_token):
    player = game.Player.players[id]
    return player if player.token.hex == hex_token else False


# Permet de générer l'identifiant du joueur
@app.route('/login', methods = ['POST'])
def login():
    player = game.Player(core)
    return jsonify(
        id = player.id,
        token = _generate_token(player),
        quote_to_find = player.quote_to_find.content,
        suggestion = player.authors_suggestion.authors
    )

# Envoie la citation et la suggestion d'auteurs
@app.route('/quotes', methods = ['POST'])
def quotes():
    id = int(request.form['id'])
    token = request.form['token']
    author_index = int(request.form['author_index'])

    player = _get_player(id, token)
    if player:

        # on donne les résultats de la question précédente
        valid_answer = int(player.check_answer(author_index))
        further_information = str(player.quote_to_find)
        # on passe à la question suivante
        player.update()
        # on envoie les informations de la question suivante
        quote_to_find = player.quote_to_find.content,
        suggestion = player.authors_suggestion.authors

        return jsonify(
            # on génère un nouveau token pour éviter que quelqu'un puisse l'intercepter
            token = _generate_token(player),

            valid_answer = valid_answer,
            further_information = further_information,
            quote_to_find = quote_to_find,
            suggestion = suggestion
        )
    else:
        return "invalid token"