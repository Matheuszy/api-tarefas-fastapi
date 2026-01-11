from fastapi import FastAPI

app = FastAPI()

from src.routers.TarefaRouter import task_router
from src.routers.UsuariosRouter import users_router

app.include_router(task_router)
app.include_router(users_router)