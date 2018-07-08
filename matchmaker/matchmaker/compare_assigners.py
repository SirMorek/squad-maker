'''
Debugging script to compare the performance of different assignment algorithms

Example invocation, from root of the project:
`
$ python -m compare_assigners
Total SSE for <function round_robin_assign_players at 0x7f442e16a950>     1307.2
Total SSE for <function greedy_assign_players at 0x7f442e16a9d8>      677.1
Total SSE for <function tree_search_assign_players at 0x7f442e16aa60>      411.2
`
'''
import json

from matchmaker.assign import (evaluate_SSE, round_robin_assign_players,
                               greedy_assign_players,
                               tree_search_assign_players)
from matchmaker.player import HockeyPlayer
from matchmaker.team import Team


def compare_assigners():
    with open("unittest/test_players.json") as player_file:
        player_json = json.loads(player_file.read())
    players = [
        HockeyPlayer.from_json(player) for player in player_json['players']
    ]

    for assigner in [
            round_robin_assign_players, greedy_assign_players,
            tree_search_assign_players
    ]:
        players_copy = players.copy()
        teams = [Team() for i in range(6)]
        remainder = assigner(players_copy, teams)
        sse = evaluate_SSE(teams)
        print("Total SSE for {assigner} {value:10.1f}".format(
            assigner=assigner, value=sum(sse)))


if __name__ == "__main__":
    exit(compare_assigners())
