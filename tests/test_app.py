import tempfile
import json
from pathlib import Path
from src import app as appmod, tasks

def test_api_create_and_list(monkeypatch):
    client = appmod.create_app().test_client()

    # cria arquivo temporário inicializado com []
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp_path = Path(tmp.name)
    tmp.close()  # fechar antes de escrever
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump([], f)

    # usa o arquivo temporário no teste
    monkeypatch.setattr(tasks, "DATA_FILE", tmp_path)

    # criar uma task
    res = client.post("/api/tasks", json={"title": "T1", "description": "d"})
    assert res.status_code == 201

    # listar tasks
    res = client.get("/api/tasks")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "T1"
