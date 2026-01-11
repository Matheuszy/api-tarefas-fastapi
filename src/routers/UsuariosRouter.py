from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.database.Database import SessionLocal
from src.schema.UsuariosSchema import UsuariosSchema
from src.service.UsuariosService import UsuarioService


users_router = APIRouter(prefix="/usuarios", tags=["user"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@users_router.post("/criar_novo_usuarios")
def create_user(
        usuario: UsuariosSchema,
        db: Session = Depends(get_db)
):
    novo_usuario = UsuarioService.create_user(db, usuario)

    if not novo_usuario:
        raise HTTPException(
            status_code=400,
            detail="Usuario já existe"
        )

    return {"mensagem: usuarip criado"}



