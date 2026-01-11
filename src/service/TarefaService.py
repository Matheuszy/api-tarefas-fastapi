from src.model.Tarefas import Tarefas


class TarefasService:
    @staticmethod
    def create_task(db, tarefa_data):
        tarefa_existente = db.query(Tarefas).filter(
            Tarefas.tarefa == tarefa_data.tarefa
        ).first()

        if tarefa_existente:
            return None

        nova_tarefa = Tarefas(
            tarefa=tarefa_data.tarefa,
            descricao=tarefa_data.descricao
        )

        db.add(nova_tarefa)
        db.commit()
        db.refresh(nova_tarefa)

        return nova_tarefa
