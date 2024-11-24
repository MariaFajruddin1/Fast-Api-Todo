# test_api.py

from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos/", json={"text": "Test Todo", "is_complete": "Test is complete"})
    assert response.status_code == 200
    assert response.json()["text"] == "Test Todo"

def test_update_todo():
    response = client.put("/todos/1", json={"text": "Updated Todo", "is_complete": "Updated for is complete"})
    assert response.status_code == 200
    assert response.json()["text"] == "Updated Todo"

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json()["message"] == "deleted Todo"