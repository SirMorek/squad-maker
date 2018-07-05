import json
from os import path

from matchmaker.main import matchmake


PLAYER_FILE = path.join(path.dirname(__file__), 'test_players.json')

def test_matchmake():
    with open(PLAYER_FILE) as player_file:
        player_json = json.loads(player_file.read())
        teams, remainder = matchmake(player_json['players'], 6)
    assert teams[0].size == teams[-1].size
    assert len(remainder) == 4
