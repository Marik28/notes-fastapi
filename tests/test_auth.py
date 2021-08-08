import pytest
from fastapi import status
from fastapi.testclient import TestClient

from notes_api.app import app

client = TestClient(app)

SIGN_UP_PATH = "/auth/sign-up/"
SIGN_IN_PATH = "/auth/sign-in/"


@pytest.fixture
def fake_user():
    return {
        "username": "test_user",
        "email": "test_email@mail.com",
        "password": "12345689sdfsdf",
    }


def test_sigh_up_with_correct_data(fake_user):
    response = client.post(SIGN_UP_PATH, json=fake_user)
    assert response.status_code == status.HTTP_201_CREATED
    assert "access_token" in response.json()


def test_sign_in_with_correct_data(fake_user):
    response = client.post(SIGN_IN_PATH, data=fake_user)
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()


def test_create_user_with_existing_data(rnd_user_data):
    response = client.post(SIGN_UP_PATH, json=rnd_user_data)
    assert response.status_code == status.HTTP_201_CREATED
    second_response = client.post(SIGN_UP_PATH, json=rnd_user_data)
    assert second_response.status_code == status.HTTP_409_CONFLICT
    assert "detail" in second_response.json()
