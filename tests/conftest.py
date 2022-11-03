import pytest
import datetime
from server import app


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
