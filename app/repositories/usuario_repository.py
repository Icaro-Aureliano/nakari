from app.models.usuario import Usuario
from app import db

class UsuarioRepository:
    @staticmethod
    def get_all():
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
        return [Usuario(*row) for row in usuarios]

    @staticmethod
    def get_by_id(cpf):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE cpf = %s", (cpf,))
        row = cursor.fetchone()
        if row:
            return Usuario(*row)
        return None

    @staticmethod
    def create(usuario):
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO usuario (cpf, senha, nome, registro) VALUES (%s, %s, %s, %s)",
                       (usuario.cpf, usuario.senha, usuario.nome, usuario.registro))
        db.connection.commit()

    @staticmethod
    def update(usuario):
        cursor = db.connection.cursor()
        cursor.execute("UPDATE usuario SET senha = %s, nome = %s, registro = %s WHERE cpf = %s",
                       (usuario.senha, usuario.nome, usuario.registro, usuario.cpf))
        db.connection.commit()

    @staticmethod
    def delete(cpf):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM usuario WHERE cpf = %s", (cpf,))
        db.connection.commit()
