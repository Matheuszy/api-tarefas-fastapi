from src.model.Usuario import Usuario


class UsuarioService():
    @staticmethod
    def create_user(db, user_data):
        user_existente = db.query(Usuario).filter(
            Usuario.username == user_data.userame
        ).first()

        if user_existente:
            return None
        else:
            novo_usuerio = Usuario(
                username = user_data.userame,
                email = user_data.email,
                senha = user_data.senha
            )

            db.add(novo_usuerio)
            db.commit(),
            db.refresh()

            return "usuário criado com sucesso" + novo_usuerio

