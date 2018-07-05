'''
Model for a Hockey Player.
'''


def get_skills(player_json):
    return {
        skill['type'].lower(): skill['rating']
        for skill in player_json['skills']
    }


class HockeyPlayer(object):
    def __init__(self, id, first_name, last_name, shooting, skating, checking):
        self._id = id
        self.first_name = first_name
        self.last_name = last_name
        self.shooting = shooting
        self.skating = skating
        self.checking = checking
        self.skill_total = self.shooting + self.skating + self.checking

    def __eq__(self, other):
        return self.skill_total == other.skill_total

    def __lt__(self, other):
        return self.skill_total < other.skill_total

    @classmethod
    def from_json(cls, player_json):
        skills = get_skills(player_json)
        return cls(player_json['_id'], player_json['firstName'],
                   player_json['lastName'], skills['shooting'],
                   skills['skating'], skills['checking'])
