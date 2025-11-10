import os
import tempfile
import json
from src import app as appmod

def test_api_create_and_list(monkeypatch):
    client = appmod.create_app().test_client()
    # ensure fresh state
    tmp = tempfile.NamedTemporaryFile(delete=False)
    monkeypatch.setattr(appmod, "DATA_FILE", tmp.name)
    # create
    res = client.post("/api/tasks", json={"title":"T1","description":"d"})
    assert res.status_code == 201
    # list
    res = client.get("/api/tasks")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)