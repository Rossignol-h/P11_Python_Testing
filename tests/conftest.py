import pytest
from server import app


# ============================================= FIXTURES


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
