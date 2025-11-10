from pathlib import Path
import tempfile
from src import tasks

def setup_function():
    tasks.DATA_FILE = Path(tempfile.gettempdir()) / "test_tasks_extra.json"
    try:
        tasks.DATA_FILE.unlink()
    except FileNotFoundError:
        pass

def teardown_function():
    try:
        tasks.DATA_FILE.unlink()
    except FileNotFoundError:
        pass

def test_update_and_delete():
    t = tasks.create_task("T", "d", "low")
    assert t.id == 1
    updated = tasks.update_task(1, title="T2", completed=True)
    assert updated is not None
    assert updated.title == "T2"
    assert updated.completed is True
    ok = tasks.delete_task(1)
    assert ok is True
    assert tasks.get_task(1) is None