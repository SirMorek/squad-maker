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

    def to_json(self):
        _json = {
            '_id': self._id,
            'firstName': self.first_name,
            'lastName': self.last_name
        }
        _json.update(self.skills_to_json())
        return _json

    def skills_to_json(self):
        return {
            'skills': [{
                'type': 'shooting',
                'rating': self.shooting
            }, {
                'type': 'skating',
                'rating': self.skating
            }, {
                'type': 'checking',
                'rating': self.checking
            }]
        }

    def __repr__(self):
        return ("{first} {last}; shooting {shooting} skating {skating} "
                "checking {checking}".format(
                    first=self.first_name,
                    last=self.last_name,
                    shooting=self.shooting,
                    skating=self.skating,
                    checking=self.checking))
