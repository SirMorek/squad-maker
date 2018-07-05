import json
from os import path

from flask import Flask

from matchmaker.main import matchmake

APP = Flask(__name__)
PLAYER_FILE = path.join(path.dirname(__file__), '..', 'players.json')


@APP.route("/")
def root():
    with open(PLAYER_FILE) as player_file:
        player_json = json.loads(player_file.read())
        teams, remainder = matchmake(player_json['players'], 6)

    return "Teams: %s\nRemainder: %s" % (teams, remainder)
