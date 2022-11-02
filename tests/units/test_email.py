import pytest


def test_login_with_known_email(client):

    response = client.post('/showSummary', data={"email": "john@simplylift.co"})
    assert response.status_code == 200
    assert response.data.decode().find('Welcome to the GUDLFT Registration Portal!')


def test_login_with_unknown_email(client):

    response = client.post('/showSummary', data={"email": "ha.ross@gmail.com"})
    assert response.status_code == 500