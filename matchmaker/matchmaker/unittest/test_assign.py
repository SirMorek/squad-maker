from matchmaker.assign import round_robin_assign_players
from matchmaker.team import Team


def test_RRAssigner_thick_teams():
    players = [i for i in range(7)]
    teams = [Team() for i in range(2)]
    leftovers = round_robin_assign_players(players, teams)
    assert len(leftovers) == 1
    assert teams[0].size == teams[1].size


def test_RRAssigner_thin_teams():
    players = [i for i in range(7)]
    teams = [Team() for i in range(6)]
    leftovers = round_robin_assign_players(players, teams)
    assert len(leftovers) == 1
    assert teams[0].size == teams[1].size


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
