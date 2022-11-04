import server


def test_purchase_under_12_places(client, mocker, clubs_fixture, competitions_fixture):
    """
        GIVEN a connected secretary's club has 15 points.
        WHEN this secretary types: 13 places to book for 
        a competition who has 20 places available,
        THEN repsponse returns status code:400 BAD REQUEST.
    """
    mocker.patch.object(server, 'clubs', clubs_fixture)
    mocker.patch.object(server, 'competitions', competitions_fixture)
    club = clubs_fixture[0]['name']
    competition = competitions_fixture[0]['name']
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 13})
    assert response.status_code == 400
