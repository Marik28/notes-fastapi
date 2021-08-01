import pytest
from fastapi import status
from fastapi.testclient import TestClient

from notes_api.app import app

client = TestClient(app)


@pytest.fixture
def fake_user():
    return {
        "username": "test_user",
        "email": "test_email@mail.com",
        "password": "12345689sdfsdf",
    }


def test_sigh_up_with_correct_data(fake_user):
    response = client.post("/auth/sign-up/", json=fake_user)
    assert response.status_code == status.HTTP_201_CREATED
    assert "access_token" in response.json()


def test_sign_in_with_correct_data(fake_user):
    response = client.post("/auth/sign-in/", data=fake_user)
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
