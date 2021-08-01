import pytest

from fastapi.testclient import TestClient
from fastapi import status
from notes_api.app import app

client = TestClient(app)
from requests.models import Response


def get_note_location(response: Response) -> str:
    return response.headers["Location"]


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


def test_create_note(token, note):
    response = client.post("/notes/", headers={"Authorization": token}, json=note)
    assert response.status_code == status.HTTP_201_CREATED
    assert "Location" in response.headers


def test_location_header_and_get_note(token, rnd_note_data):
    print(rnd_note_data)
    response = client.post("/notes/", headers={"Authorization": token}, json=rnd_note_data)
    assert "Location" in response.headers
    created_note_url = response.headers["Location"]
    response = client.get(created_note_url, headers={"Authorization": token})
    assert response.status_code == status.HTTP_200_OK
    note = response.json()
    assert rnd_note_data["title"] == note["title"]
    assert rnd_note_data["text"] == note["text"]


def test_get_notes(token):
    response = client.get("/notes/", headers={"Authorization": token})
    assert response.status_code == status.HTTP_200_OK
    assert type(response.json()) is list


def test_update_note(token, rnd_note_data):
    post_response = client.post("/notes/", headers={"Authorization": token}, json=rnd_note_data)
    created_note_url = post_response.headers["Location"]
    rnd_note_data["title"] = "changed_title"
    rnd_note_data["text"] = "changed_text"
    put_response = client.put(created_note_url, headers={"Authorization": token}, json=rnd_note_data)
    assert put_response.status_code == status.HTTP_204_NO_CONTENT
    get_response = client.get(created_note_url, headers={"Authorization": token})
    response_json = get_response.json()
    assert response_json["title"] == rnd_note_data["title"]
    assert response_json["text"] == rnd_note_data["text"]
