'''
This module is responsible for providing the ability to assign players to teams.

Assigners are expected to implement different assignment strategies, potentially
creating different team compositions.
'''
from copy import deepcopy


def evaluate_SSE(teams):
    '''
    Calculates the sum of squared errors (sse) between the teams. This is a
    useful metric by which we can talk about how large a skills gap there is
    between the teams.
    '''
    _avg_shooting = sum([team.average_shooting for team in teams]) / len(teams)
    _avg_skating = sum([team.average_skating for team in teams]) / len(teams)
    _avg_checking = sum([team.average_checking for team in teams]) / len(teams)
    SSE_shooting = sum(
        [(team.average_shooting - _avg_shooting)**2 for team in teams])
    SSE_skating = sum(
        [(team.average_skating - _avg_skating)**2 for team in teams])
    SSE_checking = sum(
        [(team.average_checking - _avg_checking)**2 for team in teams])
    return (SSE_shooting, SSE_skating, SSE_checking)


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


def tree_search_assign_players(players, teams):
    '''
    Assign players to teams such that teams are equally sized.

    Assign the players to the team that (locally) minimizes the skill spread.
    '''
    num_teams = len(teams)
    if num_teams == 0:
        return players

    players.sort(reverse=True)
    num_players = len(players)
    while len(players) > num_players % num_teams:
        min_size = min([team.size for team in teams])
        player = players.pop()
        team_errors = []
        for index, team in enumerate(teams):
            if team.size != min_size:
                continue
            teams_copy = deepcopy(teams)
            teams_copy[index].add_player(player)
            errors = evaluate_SSE(teams_copy)
            team_errors.append((index, errors))
        index, error = min(team_errors, key=lambda x: x[1])
        teams[index].add_player(player)
    return players
