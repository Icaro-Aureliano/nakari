from flask import current_app

class TerceiroService:
    @staticmethod
    def get_all_terceiros():
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM terceiros")
        terceiros = cursor.fetchall()
        cursor.close()
        return terceiros
    
    @staticmethod
    def get_terceiro_by_coc(coc):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM terceiros WHERE coc = %s", (coc,))
        terceiro = cursor.fetchone()
        cursor.close()
        return terceiro
    
    @staticmethod
    def create_terceiro(**data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "INSERT INTO terceiros (coc, razao, telefone, endereco, email, status, servico, preco) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (data['coc'], data['razao'], data['telefone'], data['endereco'], data['email'], data['status'], data['servico'], data['preco']))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def update_terceiro(coc, data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        print(data)
        query = "UPDATE terceiros SET coc=%s, razao=%s, telefone=%s, endereco=%s, email=%s, status=%s, servico=%s, preco=%s WHERE coc=%s"
        cursor.execute(query, (data['coc'], data['razao'], data['telefone'], data['endereco'], data['email'], data['status'], data['servico'], data['preco'], coc))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def delete_terceiro(coc):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM terceiros WHERE coc = %s", (coc,))
        db.connection.commit()
        cursor.close()
