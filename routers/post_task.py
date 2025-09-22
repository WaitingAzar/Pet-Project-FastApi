from fastapi import APIRouter, HTTPException
from DataBase import container
from models.tasks import Tasks
import uuid

router = APIRouter(prefix="/tasks", tags=["tasks post"])

@router.post("/create_tasks")
def create_tasks(task: Tasks):
    try:
        container.create_item(body=dict(task))
        return {"message": "Task created", "id": task.id}
    except Exception as e:
        # Повертаємо повну помилку для дебагу
        raise HTTPException(status_code=500, detail=str(e))
