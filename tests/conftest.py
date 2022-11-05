import pytest
import datetime
from server import app
import server

# ============================================= FIXTURES


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# @pytest.fixture
# def current_date():
#     now = datetime.datetime.now()
#     return now.strftime("%Y-%m-%d, %H:%M:%S")


@pytest.fixture
def clubs_fixture():
    return [
        {
            "name": "Basic lift",
            "email": "john@basiclift.co",
            "points": "15"
        },
        {
            "name": "BeastMaster",
            "email": "admin@beastmaster.com",
            "points": "20"
        },
        {
            "name": "Urban fit",
            "email": "Tom@urbanfit.co.uk",
            "points": "6"
        }
    ]


@pytest.fixture
def unknown_club():
    return [
        {
            "name": "Fake club",
            "email": "sam@email.co",
            "points": "12"
        },
        {
            "name": "Unknown Club",
            "email": "jim@gmail.com",
            "points": "9"
        },
        {
            "name": "invisible Club",
            "email": "sarah@yahoo.co.uk",
            "points": "16"
        }
    ]


@pytest.fixture
def competitions_fixture():
    return [
        {
            "name": "Aka League",
            "date": "2023-02-05 10:00:00",
            "numberOfPlaces": "20"
        },
        {
            "name": "Pink Race",
            "date": "2021-05-12 09:00:00",
            "numberOfPlaces": "4"
        },
        {
            "name": "Champion Road",
            "date": "2022-10-13 13:00:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Ice Race",
            "date": "2022-12-01 14:00:00",
            "numberOfPlaces": "10"
        }
    ]

@pytest.fixture
def cart_fixture(competitions_fixture, clubs_fixture):
    return {
    competition["name"]: {club["name"]: 0 for club in clubs_fixture}
    for competition in competitions_fixture
}


@pytest.fixture
def fixture(mocker, clubs_fixture, competitions_fixture, cart_fixture):
    return [mocker, clubs_fixture, competitions_fixture, cart_fixture]


def get(fixture, case , places=0):
    fixture[0].patch.object(server, 'clubs', fixture[1])
    fixture[0].patch.object(server, 'competitions', fixture[2])
    fixture[0].patch.object(server, 'cart', fixture[3])

    if case == "email":

        email = fixture[1][0]['email']
        data_email = {'email': email}
        return data_email

    elif case == "club_competition":
        
        club = fixture[1][0]['name']
        competition = fixture[2][0]['name']
        data_book = {'competition': competition, 'club': club}
        return data_book

    elif case == "club_competition_places":
        
        club = fixture[1][0]['name']
        competition = fixture[2][0]['name']
        data_purchase_places = {'competition': competition, 'club': club, 'places': places}
        return data_purchase_places

    elif case == "board":

        return  fixture[1]
