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


def test_board_with_no_data(client, mocker):
    """
        GIVEN any user,
        WHEN he/she goes to '/board' with GET method & no data return,
        THEN an error message will display.
    """
    mocker.patch.object(server, 'clubs', '')
    response = client.get('/board')
    assert response.status_code == 200
    assert b'<p> Sorry, this section has no clubs to display</p>' in response.data
