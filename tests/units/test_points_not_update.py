import server


def test_points_update_correctly(client, mocker, clubs_fixture, competitions_fixture):
    """
        GIVEN a connected secretary's club has 15 points,
        he/she purchased 5 places,
        for a competition who has 20 places available,
        WHEN this secretary click on book button, 
        THEN club's points are updated 
    """
    mocker.patch.object(server, 'clubs', clubs_fixture)
    mocker.patch.object(server, 'competitions', competitions_fixture)
    
    club = clubs_fixture[0]
    competition = competitions_fixture[0]['name']
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club['name'], 'places': 5})

    assert response.status_code == 200
    assert f"Points available: {club['points']}" in response.data.decode()
