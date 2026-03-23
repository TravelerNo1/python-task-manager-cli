import json
from task import Task

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    except:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([task.to_dict() for task in tasks], f, ensure_ascii=False, indent=4)