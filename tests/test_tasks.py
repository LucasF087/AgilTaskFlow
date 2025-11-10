import os, tempfile
from src import tasks

def setup_function():
    tasks.DATA_FILE = os.path.join(tempfile.gettempdir(), "test_tasks.json")
    try:
        os.remove(tasks.DATA_FILE)
    except:
        pass

def teardown_function():
    try:
        os.remove(tasks.DATA_FILE)
    except:
        pass

def test_create_and_get():
    t = tasks.create_task("Test Task", "desc", "high")
    assert t.id == 1
    g = tasks.get_task(1)
    assert g is not None
    assert g.title == "Test Task"