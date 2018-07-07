from matchmaker.player import get_skills, HockeyPlayer

SAMPLE_PLAYER = {
    "_id":
    "5a845e2a307ab9c4446eb195",
    "firstName":
    "Cristina",
    "lastName":
    "Moses",
    "skills": [{
        "type": "Shooting",
        "rating": 26
    }, {
        "type": "Skating",
        "rating": 80
    }, {
        "type": "Checking",
        "rating": 65
    }]
}

DUMMY_SKILLS_JSON = {
    "skills": [{
        "type": "foo",
        "rating": -5
    }, {
        "type": "bAR",
        "rating": 1000
    }, {
        "type": "BAZ",
        "rating": "turnip"
    }]
}

SAMPLE_PLAYER_2 = {
    "_id":
    "5a845e2aed91d892ea2973de",
    "firstName":
    "Brown",
    "lastName":
    "Nash",
    "skills": [{
        "type": "Shooting",
        "rating": 30
    }, {
        "type": "Skating",
        "rating": 58
    }, {
        "type": "Checking",
        "rating": 76
    }]
}


def test_get_skills():
    skills = get_skills(SAMPLE_PLAYER)
    assert skills['shooting'] == 26
    assert skills['skating'] == 80
    assert skills['checking'] == 65
    assert len(skills.keys()) == 3


def test_get_skills_dummy():
    skills = get_skills(DUMMY_SKILLS_JSON)
    assert skills['foo'] == -5
    assert skills['bar'] == 1000
    assert skills['baz'] == 'turnip'


def test_hockey_player_from_json():
    player = HockeyPlayer.from_json(SAMPLE_PLAYER)
    assert player.first_name == "Cristina"
    assert player.last_name == "Moses"
    assert player.shooting == 26
    assert player.skating == 80
    assert player.checking == 65
    assert player.skill_total == 171


def test_hockey_player_to_from_json():
    player = HockeyPlayer.from_json(SAMPLE_PLAYER)
    dump = player.to_json()
    player2 = HockeyPlayer.from_json(dump)
    assert player == player2


def test_hockey_player_sort():
    player_1 = HockeyPlayer.from_json(SAMPLE_PLAYER)
    player_2 = HockeyPlayer.from_json(SAMPLE_PLAYER_2)
    assert player_1 > player_2
    assert sorted([player_1, player_2]) == [player_2, player_1]
