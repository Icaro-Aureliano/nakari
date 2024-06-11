from flask import current_app

class UsuarioService:
    @staticmethod
    def get_all_usuarios():
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios
    
    @staticmethod
    def get_usuario_by_cpf(cpf):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE cpf = %s", (cpf,))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario
    
    @staticmethod
    def create_usuario(**data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "INSERT INTO usuario (cpf, senha, nome, registro) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['cpf'], data['senha'], data['nome'], data['registro']))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def update_usuario(cpf, **data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "UPDATE usuario SET senha=%s, nome=%s, registro=%s WHERE cpf=%s"
        cursor.execute(query, (data['senha'], data['nome'], data['registro'], int(cpf)))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def delete_usuario(cpf):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM usuario WHERE cpf = %s", (cpf,))
        db.connection.commit()
        cursor.close()
