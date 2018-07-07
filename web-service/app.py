import json
from os import path

from flask import Flask, render_template

from matchmaker.main import matchmake
from matchmaker.team import Team
from matchmaker.player import HockeyPlayer

APP = Flask(__name__)
PLAYER_FILE = path.join(path.dirname(__file__), '..', 'players.json')
PERSISTENCE_FILE = path.join(path.dirname(__file__), 'persistence.json')


@APP.route("/")
def root():
    with open(PLAYER_FILE) as player_file:
        player_json = json.loads(player_file.read())
        teams, players = matchmake(player_json['players'], 6)

    with open(PERSISTENCE_FILE, "w") as outfile:
        outfile.write(
            json.dumps({
                "teams": Team.bulk_to_json(teams),
                "players": [player.to_json() for player in players]
            }))

    return render_template('base.html', teams=teams, players=players)


@APP.route("/teams", methods=["GET", "POST"])
def view():
    try:
        with open(PERSISTENCE_FILE) as cache:
            cache_results = json.loads(cache.read())
            players = cache_results['players']
            teams = cache_results['teams']
        players = [
            HockeyPlayer.from_json(player_json) for player_json in players
        ]
        teams = [Team.from_json(team_json) for team_json in teams]
    except FileNotFoundError as e:
        with open(PLAYER_FILE) as player_file:
            _player_json = json.loads(player_file.read())
            players = [
                HockeyPlayer.from_json(player_json)
                for player_json in _player_json['players']
            ]
            teams = []
    return render_template('base.html', teams=teams, players=players)
