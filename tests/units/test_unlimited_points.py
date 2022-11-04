import server


def test_purchase_with_enough_points(client, mocker, clubs_fixture, competitions_fixture):
    """
        GIVEN a connected secretary's club has 6 points.
        WHEN this secretary types: 8 places to book for 
        a competition who has 20 places available,
        THEN the places are successfully purchased with success message.
    """
    mocker.patch.object(server, 'clubs', clubs_fixture)
    mocker.patch.object(server, 'competitions', competitions_fixture)
    club = clubs_fixture[2]['name']
    competition = competitions_fixture[0]['name']
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 3})
    assert response.status_code == 200


def test_purchase_not_enough_points(client, mocker, clubs_fixture, competitions_fixture):
    """
        GIVEN a connected secretary's club has 6 points.
        WHEN this secretary types: 8 places to book for 
        a competition who has 20 places available,
        THEN response with status code:400 BAD REQUEST.
    """
    mocker.patch.object(server, 'clubs', clubs_fixture)
    mocker.patch.object(server, 'competitions', competitions_fixture)
    club = clubs_fixture[2]['name']
    competition = competitions_fixture[0]['name']
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 8})
    assert response.status_code == 400