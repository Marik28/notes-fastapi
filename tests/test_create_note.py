import pytest
from fastapi import status
from fastapi.testclient import TestClient
from requests.models import Response

from notes_api.app import app

client = TestClient(app)

CREATE_NOTE_PATH = "/notes/"


def get_note_location(response: Response) -> str:
    return response.headers["Location"]


def test_unauthorized_create_note(rnd_note_data):
    response = client.post(CREATE_NOTE_PATH, json=rnd_note_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "detail" in response.json()


def test_successful_create_note(token, note):
    response = client.post(CREATE_NOTE_PATH, headers={"Authorization": token}, json=note)
    assert response.status_code == status.HTTP_201_CREATED
    assert "Location" in response.headers


def test_response_has_correct_location_header(token, rnd_note_data):
    print(rnd_note_data)
    response = client.post(CREATE_NOTE_PATH, headers={"Authorization": token}, json=rnd_note_data)
    assert "Location" in response.headers
    created_note_url = response.headers["Location"]
    response = client.get(created_note_url, headers={"Authorization": token})
    assert response.status_code == status.HTTP_200_OK
    note = response.json()
    assert rnd_note_data["title"] == note["title"]
    assert rnd_note_data["text"] == note["text"]
