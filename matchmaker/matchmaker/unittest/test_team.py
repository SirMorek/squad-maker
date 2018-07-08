from matchmaker.team import Team
from matchmaker.player import HockeyPlayer


def test_team():
    team = Team()
    assert team.size == 0
    assert team.average_shooting == 0
    assert team.average_skating == 0
    assert team.average_checking == 0


def test_team_averages():
    team = Team()
    player = HockeyPlayer(0, 'a', 'b', 10, 10, 20)
    team.add_player(player)
    assert team.average_shooting == 10
    assert team.average_skating == 10
    assert team.average_checking == 20

    player2 = HockeyPlayer(1, 'c', 'd', 20, 20, 40)
    team.add_player(player2)
    assert team.average_shooting == 15
    assert team.average_skating == 15
    assert team.average_checking == 30
