import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Homepage should load and show login link"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Login Page" in response.data

def test_login_success(client):
    """Login with correct credentials should succeed"""
    response = client.post("/login", data={"username": "admin", "password": "1234"})
    assert response.status_code == 200
    assert b"Welcome back, admin!" in response.data

def test_login_failure(client):
    """Login with wrong credentials should fail"""
    response = client.post("/login", data={"username": "wrong", "password": "wrong"})
    assert response.status_code == 200
    assert b"Invalid credentials" in response.data
