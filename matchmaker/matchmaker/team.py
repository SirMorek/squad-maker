'''
Simple structures for tracking teams.

Expected to have some basic ability to make it easy to add, remove and try out
players while sorting out players.
'''


class Team(object):
    def __init__(self, name=None):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    @property
    def size(self):
        return len(self.players)
