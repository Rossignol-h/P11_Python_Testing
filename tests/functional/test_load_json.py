from server import loadClubs, loadCompetitions


def test_load_json():
    """
        GIVEN json files as database for flask app
        WHEN a user make a request that needed clubs & competitons data
        THEN all the data is correctly loaded
    """
    clubs = loadClubs()
    assert clubs is not None
    assert isinstance(clubs, list)
    assert len(clubs) > 0

    competitions = loadCompetitions()
    assert competitions is not None
    assert isinstance(competitions, list)
    assert len(competitions) > 0
