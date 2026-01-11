from sqlalchemy import String
from src.database.Database import Base
from sqlalchemy import Integer, Column



class Tarefas(Base):
    __tablename__ = "tarefas"

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    tarefa = Column("task",String(40), nullable=False)
    descricao = Column("description", String(150), nullable=False)

