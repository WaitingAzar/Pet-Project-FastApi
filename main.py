from fastapi import FastAPI
import uvicorn
from routers import post_task

app = FastAPI(title="Tasks API")

# Підключаємо роутер
app.include_router(post_task.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)