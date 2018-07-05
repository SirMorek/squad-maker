'''
This module is responsible for providing the ability to assign players to teams.

Assigners are expected to implement different assignment strategies, potentially
creating different team compositions.
'''


def round_robin_assign_players(players, teams):
    '''
    A basic team builder that simply round-robins through the provided players
    and makes no attempt to balance the teams.

    Assigns many players as possible to teams, such that teams are equally
    sized. Assume teams have no players on them initially.
    '''
    num_teams = len(teams)
    if num_teams == 0:
        return players

    team_index = 0
    num_players = len(players)
    while len(players) > num_players % num_teams:
        player = players.pop()
        teams[team_index].add_player(player)
        team_index = (team_index + 1) % num_teams
    return players
