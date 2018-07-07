from random import randint

from matchmaker.assign import round_robin_assign_players, greedy_assign_players
from matchmaker.team import Team
from matchmaker.player import HockeyPlayer


def _generate_players(num_players):
    return [
        HockeyPlayer(i, i, i, randint(1, 100), randint(1, 100), randint(
            1, 100)) for i in range(num_players)
    ]


def test_RRAssigner_thick_teams():
    players = _generate_players(7)
    teams = [Team() for i in range(2)]
    leftovers = round_robin_assign_players(players, teams)
    assert len(leftovers) == 1
    assert max([team.size for team in teams]) == min(
        [team.size for team in teams])


def test_RRAssigner_thin_teams():
    players = _generate_players(7)
    teams = [Team() for i in range(6)]
    leftovers = round_robin_assign_players(players, teams)
    assert len(leftovers) == 1
    assert max([team.size for team in teams]) == min(
        [team.size for team in teams])


def test_RRAssigner_no_teams():
    players = [i for i in range(7)]
    teams = []
    leftovers = round_robin_assign_players(players, teams)
    assert leftovers == players


def test_RRAssigner_no_players():
    players = []
    teams = [Team() for i in range(2)]
    leftovers = round_robin_assign_players(players, teams)
    assert leftovers == players


def test_GreedyAssigner_thick_teams():
    players = _generate_players(7)
    teams = [Team() for i in range(2)]
    leftovers = greedy_assign_players(players, teams)
    assert len(leftovers) == 1
    assert max([team.size for team in teams]) == min(
        [team.size for team in teams])


def test_GreedyAssigner_thin_teams():
    players = _generate_players(7)
    teams = [Team() for i in range(6)]
    leftovers = greedy_assign_players(players, teams)
    assert len(leftovers) == 1
    assert max([team.size for team in teams]) == min(
        [team.size for team in teams])


def test_GreedyAssigner_no_teams():
    players = [i for i in range(7)]
    teams = []
    leftovers = greedy_assign_players(players, teams)
    assert leftovers == players


def test_GreedyAssigner_no_players():
    players = []
    teams = [Team() for i in range(2)]
    leftovers = greedy_assign_players(players, teams)
    assert leftovers == players
