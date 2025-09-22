from fastapi import APIRouter, HTTPException
from DataBase import container
from models.tasks import Tasks
import uuid

router = APIRouter(prefix="/tasks", tags=["tasks get"])

@router.get("/get_tasks")
def get_tasks():
  all_tasks = list(container.query_items(
    query="SELECT * FROM c",
    enable_cross_partition_query=True
    ))
  return all_tasks
