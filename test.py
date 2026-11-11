import pytest
from app import add_numbers, app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0


def test_home_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["status"] == "running"


def test_add_endpoint_valid(client):
    response = client.get("/add?a=10&b=15")
    assert response.status_code == 200
    assert response.get_json()["result"] == 25


def test_add_endpoint_invalid(client):
    response = client.get("/add?a=abc&b=5")
    assert response.status_code == 400
