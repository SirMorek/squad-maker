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


def greedy_assign_players(players, teams):
    '''
    A team builder that attempts to avoid stacking teams by assigning the
    strongest players first.

    Assign the players in descending order of total skill rating.
    Always assign to the team with the lowest total skill rating first.
    Assign players to teams such that teams are equally sized.
    '''
    num_teams = len(teams)
    if num_teams == 0:
        return players

    players.sort(reverse=True)
    num_players = len(players)
    while len(players) > num_players % num_teams:
        player = players.pop()
        min_size = min([team.size for team in teams])
        candidate_teams = [team for team in teams if team.size == min_size]
        candidate_teams.sort()
        candidate_teams[0].add_player(player)
    return players
