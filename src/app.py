from fastapi import FastAPI

app = FastAPI()

from src.routers.TarefaRouter import task_router

app.include_router(task_router)