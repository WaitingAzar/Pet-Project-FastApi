from fastapi import APIRouter, HTTPException
from DataBase import container
from azure.cosmos import exceptions

router = APIRouter(prefix="/tasks", tags=["tasks delete"])

@router.delete("/delete_task/{task_id}")
def delete_task(task_id: str):
    try:
        # partition_key = id, тому передаємо task_id для обох параметрів
        container.delete_item(item=task_id, partition_key=task_id)
        return {"message": f"Task {task_id} deleted"}
    except exceptions.CosmosResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
