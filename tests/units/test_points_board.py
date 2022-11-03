import server

def test_display_points_board(client, mocker, clubs_fixture):
    """
        GIVEN any user,
        WHEN he/she goes to '/board',
        THEN a board will display with all clubs and their points.
    """
    mocker.patch.object(server, 'clubs', clubs_fixture)
    response = client.get('/board')
    assert response.status_code == 200
    assert f"<td>{clubs_fixture[0]['name']}</td>" in response.data.decode()
