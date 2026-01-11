from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:matheusted19@localhost:5432/tarefas_db"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("Conectado com sucesso!")