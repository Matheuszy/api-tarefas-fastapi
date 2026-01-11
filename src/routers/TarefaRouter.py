from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.database.Database import SessionLocal
from src.schema.TarefasSchema import TarefasSchema
from src.service.TarefaService import TarefasService


task_router = APIRouter(prefix="/tarefas", tags=["task"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@task_router.post("/criar")
def criar_tarefa(
        tarefa: TarefasSchema,
        db: Session = Depends(get_db)
):
    nova_tarefa = TarefasService.create_task(db, tarefa)

    if not nova_tarefa:
        raise HTTPException(
            status_code=400,
            detail="Tarefa já existe"
        )

    return {"mensagem": "Tarefa criada com sucesso"}