from dataclasses import dataclass, asdict
from typing import List, Optional
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "tasks.json"
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = ""
    completed: bool = False
    priority: Optional[str] = "medium"

def _read_all() -> List[Task]:
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:  # arquivo não existe ou vazio
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return [Task(**item) for item in raw]

def _write_all(tasks: List[Task]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tasks], f, indent=2, ensure_ascii=False)

def list_tasks() -> List[Task]:
    return _read_all()

def get_task(task_id: int) -> Optional[Task]:
    return next((t for t in _read_all() if t.id == task_id), None)

def create_task(title: str, description: str = "", priority: str = "medium") -> Task:
    tasks = _read_all()
    next_id = max((t.id for t in tasks), default=0) + 1
    task = Task(id=next_id, title=title, description=description, priority=priority)
    tasks.append(task)
    _write_all(tasks)
    return task

def update_task(task_id: int, title: Optional[str]=None, description: Optional[str]=None,
                completed: Optional[bool]=None, priority: Optional[str]=None) -> Optional[Task]:
    tasks = _read_all()
    for i, t in enumerate(tasks):
        if t.id == task_id:
            if title is not None: t.title = title
            if description is not None: t.description = description
            if completed is not None: t.completed = completed
            if priority is not None: t.priority = priority
            tasks[i] = t
            _write_all(tasks)
            return t
    return None

def delete_task(task_id: int) -> bool:
    tasks = _read_all()
    new_tasks = [t for t in tasks if t.id != task_id]
    if len(new_tasks) == len(tasks):
        return False
    _write_all(new_tasks)
    return True
