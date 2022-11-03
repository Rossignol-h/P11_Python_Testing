import server


def test_purchase_futur_competition(client, mocker, clubs_fixture, competitions_fixture):
    """
        GIVEN a connected secretary's club wants to book places in a futur competition.
        date of this competition = "2023-02-05 10:00:00".
        WHEN this secretary types: 5 places
        THEN places are pruchased with status code:200.
    """
    mocker.patch.object(server, 'clubs', clubs_fixture)
    mocker.patch.object(server, 'competitions', competitions_fixture)
    club = clubs_fixture[0]['name']
    competition = competitions_fixture[0]['name']
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 5})
    assert response.status_code == 200


def test_purchase_past_competition(client, mocker, clubs_fixture, competitions_fixture):
    """
        GIVEN a connected secretary's club wants to book places in a past competition.
        date of this competition = "2021-05-12 09:00:00".
        WHEN this secretary types: 5 places
        THEN an error message displays, with status code:400 BAD REQUEST.
    """
    mocker.patch.object(server, 'clubs', clubs_fixture)
    mocker.patch.object(server, 'competitions', competitions_fixture)
    club = clubs_fixture[0]['name']
    competition = competitions_fixture[1]['name']
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 5})
    assert response.status_code == 400
    assert b'Sorry, this competition is over !' in response.data
