from flask import current_app

class EspacoService:
    @staticmethod
    def get_all_espacos():
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM espacos")
        espacos = cursor.fetchall()
        cursor.close()
        return espacos
    
    @staticmethod
    def get_espaco_by_id(codigo):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM espacos WHERE codigo = %s", (codigo,))
        espaco = cursor.fetchone()
        cursor.close()
        return espaco
    
    @staticmethod
    def create_espaco(**data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "INSERT INTO espacos (nome, ds, status, capacidade) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['nome'], data['ds'], data['status'], data['capacidade']))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def update_espaco(codigo, **data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "UPDATE espacos SET nome=%s, ds=%s, status=%s, capacidade=%s WHERE codigo=%s"
        cursor.execute(query, (data['nome'], data['ds'], data['status'], data['capacidade'], codigo))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def delete_espaco(codigo):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM espacos WHERE codigo = %s", (codigo,))
        db.connection.commit()
        cursor.close()
