from pydantic import BaseModel


class UsuariosSchema(BaseModel):
        username: str
        email: str
        senha: str

class Config:
    from_attributes = True