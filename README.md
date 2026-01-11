# 📝 API de Tarefas — FastAPI + SQLAlchemy + Alembic

Este projeto é uma **API simples de gerenciamento de tarefas**, desenvolvida com o objetivo de **testar e estudar o framework FastAPI**, bem como a integração com **SQLAlchemy**, **Alembic** e **PostgreSQL**.

A ideia principal foi criar algo **enxuto e funcional**, focando em entender a arquitetura, fluxo de dados, migrations e organização de um projeto backend moderno em Python.

---

## 🚀 Tecnologias utilizadas

- **Python 3**
- **FastAPI**
- **SQLAlchemy**
- **Alembic**
- **PostgreSQL**
- **Pydantic**
- **Uvicorn**

---

## 📂 Estrutura do projeto

api-tarefas/
├── alembic/
│ ├── versions/
│ ├── env.py
│ └── script.py.mako
├── src/
│ ├── database/
│ ├── model/
│ ├── routers/
│ ├── schema/
│ ├── service/
│ └── app.py
├── .env
├── .gitignore
└── README.md


A separação foi pensada para manter uma **organização clara por responsabilidade**, facilitando manutenção e futuras evoluções.

---

## ⚙️ Funcionalidades atuais

- Criar tarefas
- Validação básica de dados
- Persistência em banco de dados
- Controle de versões do banco via Alembic

---

## 🗄️ Banco de dados e migrations

O projeto utiliza **Alembic** para versionamento do schema do banco de dados.

Com o banco configurado corretamente, basta rodar:

```bash
````

alembic upgrade head
🔐 Observação importante

Este projeto foi feito de forma propositalmente simples, apenas para testar o framework e o fluxo de desenvolvimento.

❌ Ainda NÃO implementado

Login de usuários

Autenticação

Autorização

Criptografia de dados sensíveis

Controle de permissões

✅ Planejado para futuras versões

Autenticação com JWT

Criptografia de senhas

Camada de segurança (roles e permissões)

Dockerização

Testes automatizados

como rodar:
python -m venv .venv

instale as dependências
pip install -r requirements.txt

configure o .env

DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/tarefas_db

rode as migrations
alembic upgrade head

execute a aplicação
uvicorn src.app:app --reload


👤 Autor

Desenvolvido por Matheus Carlos
Projeto de estudo e experimentação com FastAPI.

