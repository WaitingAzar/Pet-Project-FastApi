from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import get_task_json, post_task, get_task,  delete_task,login

app = FastAPI(title="Tasks API")

app.include_router(login.router)
app.include_router(post_task.router)
app.include_router(get_task.router)
app.include_router(delete_task.router)
app.include_router(get_task_json.router)
# підключаємо папку templates
templates = Jinja2Templates(directory="templates")

# підключаємо папку static (для CSS, JS, картинок)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)