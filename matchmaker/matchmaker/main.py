'''
The matchmaker service is responsible for taking the set of players and
producing a list of teams, plus the "wait list" of the remaining players who
could not be fit on a team.
'''
from matchmaker.assign import round_robin_assign_players
from matchmaker.player import HockeyPlayer
from matchmaker.team import Team


def matchmake(player_list, num_teams):
    players = [HockeyPlayer.from_json(player) for player in player_list]
    teams = [Team() for i in range(num_teams)]
    remainder = round_robin_assign_players(players, teams)
    return teams, remainder
