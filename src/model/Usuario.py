from sqlalchemy import String
from src.database.Database import Base
from sqlalchemy import Integer, Column

class Usuario(Base):
    __tablename__="usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String(150), unique=True, nullable=False)
    email = Column("email",String(250), unique=True, nullable=False)
    senha = Column("senha", String, nullable=False)
