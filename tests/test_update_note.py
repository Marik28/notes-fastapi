from fastapi import status
from fastapi.testclient import TestClient

from notes_api.app import app

client = TestClient(app)

UPDATE_NOTE_PATH = "/notes/"


def test_update_note(token, rnd_note_data):
    post_response = client.post(UPDATE_NOTE_PATH, headers={"Authorization": token}, json=rnd_note_data)
    created_note_url = post_response.headers["Location"]
    rnd_note_data["title"] = "changed_title"
    rnd_note_data["text"] = "changed_text"
    put_response = client.put(created_note_url, headers={"Authorization": token}, json=rnd_note_data)
    assert put_response.status_code == status.HTTP_204_NO_CONTENT
    get_response = client.get(created_note_url, headers={"Authorization": token})
    response_json = get_response.json()
    assert response_json["title"] == rnd_note_data["title"]
    assert response_json["text"] == rnd_note_data["text"]
