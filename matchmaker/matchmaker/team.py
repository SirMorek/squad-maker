'''
Simple structures for tracking teams.

Expected to have some basic ability to make it easy to add, remove and try out
players while sorting out players.
'''

from matchmaker.player import HockeyPlayer


class Team(object):
    def __init__(self, name=None):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    @property
    def size(self):
        return len(self.players)

    def __repr__(self):
        return "Team {name}: {players}".format(
            name=self.name, players=self.players)

    @classmethod
    def from_json(cls, team_json):
        team = Team(name=team_json['name'])
        team.players = [
            HockeyPlayer.from_json(player_json)
            for player_json in team_json['players']
        ]
        return team

    def to_json(self):
        return {
            'name': self.name,
            'players': [player.to_json() for player in self.players]
        }

    @staticmethod
    def bulk_to_json(team_list):
        return [team.to_json() for team in team_list]
