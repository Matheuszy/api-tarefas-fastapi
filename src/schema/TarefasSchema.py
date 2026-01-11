from pydantic import  BaseModel

class TarefasSchema(BaseModel):
        tarefa:str
        descricao:str


class Config:
        from_attributes = True
