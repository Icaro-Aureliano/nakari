from flask import current_app

class MoradorService:
    @staticmethod
    def get_all_moradores():
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM moradores")
        moradores = cursor.fetchall()
        cursor.close()
        return moradores
    
    @staticmethod
    def get_morador_by_cpf(cpf):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM moradores WHERE cpf = %s", (cpf,))
        morador = cursor.fetchone()
        cursor.close()
        return morador
    
    @staticmethod
    def create_morador(**data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "INSERT INTO moradores (cpf, nome, torre, andar, apartamento, email, telefone, moradorescol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (data['cpf'], data['nome'], data['torre'], data['andar'], data['apartamento'], data['email'], data['telefone'], data['moradorescol']))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def update_morador(cpf, **data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "UPDATE moradores SET nome=%s, torre=%s, andar=%s, apartamento=%s, email=%s, telefone=%s, moradorescol=%s WHERE cpf=%s"
        cursor.execute(query, (data['nome'], data['torre'], data['andar'], data['apartamento'], data['email'], data['telefone'], data['moradorescol'], cpf))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def delete_morador(cpf):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM moradores WHERE cpf = %s", (cpf,))
        db.connection.commit()
        cursor.close()
