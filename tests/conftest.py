import random

import pytest
from fastapi.testclient import TestClient

from notes_api.app import app
from notes_api.models.auth import Token

client = TestClient(app)


@pytest.fixture
def rnd_int_gen():
    return random.Random(123456)


@pytest.fixture(scope="session")
def user():
    user_data = {
        "username": "test_user",
        "email": "test_email@mail.com",
        "password": "12345689sdfsdf",
    }
    client.post("/auth/sign-up/", json=user_data)
    return user_data


@pytest.fixture(scope="session")
def rnd_user_data(rnd_int_gen):
    return {
        "username": f"test_user-{rnd_int_gen.randint(1000, 9999)}",
        "email": f"test_email-{rnd_int_gen.randint(1000, 9999)}@mail.com",
        "password": f"password{rnd_int_gen.randint(1000, 9999)}",
    }


@pytest.fixture
def note():
    return {
        "title": 'dsfsdfs',
        "text": "sdfsdjfposidfusdof"
    }


@pytest.fixture
def rnd_note_data(rnd_int_gen):
    return {
        "title": str(rnd_int_gen.randint(1000, 9999)),
        "text": str(rnd_int_gen.randint(1000, 9999)),
    }


@pytest.fixture(scope="session")
def token(user):
    response = client.post("/auth/sign-in/", data=user)
    response_json = response.json()
    access_token = Token(**response_json)
    return f"{access_token.token_type.upper()} {access_token.access_token}"
