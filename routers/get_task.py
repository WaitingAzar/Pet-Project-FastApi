from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from DataBase import container

router = APIRouter(prefix="/tasks", tags=["tasks get"])
templates = Jinja2Templates(directory="templates")

@router.get("/show_tasks")
def show_tasks(request: Request):
    all_tasks = list(container.query_items(
        query="SELECT * FROM c",
        enable_cross_partition_query=True
    ))
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": all_tasks})
