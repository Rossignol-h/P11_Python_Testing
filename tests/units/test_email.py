import pytest
import server


def test_login_with_known_email(client, mocker, clubs_fixture):
    """
        GIVEN a user not connected
        WHEN a user types in an email found in the system
        THEN this user is successfully connected
    """
    mocker.patch.object(server, 'clubs', clubs_fixture)
    response = client.post('/showSummary', data=clubs_fixture[0])
    assert response.status_code == 200
    assert response.data.decode().find('Welcome to the GUDLFT Registration Portal!')


def test_login_with_unknown_email(client, unknown_club):
    """
        GIVEN a user not connected
        WHEN a user types in an email which is not found in the system
        THEN the error is caught and handled with error message
    """
    response = client.post('/showSummary', data=unknown_club[0])
    assert response.status_code == 302
    with pytest.raises(Exception) as exc_info:
        assert str(exc_info.value) == "Sorry, this email wasn't found. Please try again with a correct email !!"
