import tempfile
from pathlib import Path
from src import tasks

def setup_function():
    # define DATA_FILE temporário
    tasks.DATA_FILE = Path(tempfile.gettempdir()) / "test_tasks.json"
    try:
        tasks.DATA_FILE.unlink()  # remove se existir
    except FileNotFoundError:
        pass

def teardown_function():
    try:
        tasks.DATA_FILE.unlink()
    except FileNotFoundError:
        pass

def test_create_and_get():
    t = tasks.create_task("Test Task", "desc", "high")
    assert t.id == 1
    g = tasks.get_task(1)
    assert g is not None
    assert g.title == "Test Task"
