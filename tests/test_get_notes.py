from fastapi import status
from fastapi.testclient import TestClient

from notes_api.app import app

client = TestClient(app)
GET_NOTES_PATH = "/notes/"


def test_get_notes(token):
    response = client.get(GET_NOTES_PATH, headers={"Authorization": token})
    assert response.status_code == status.HTTP_200_OK
    assert type(response.json()) is list
