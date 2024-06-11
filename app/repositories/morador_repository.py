from app.models.morador import Morador
from app import db

class MoradorRepository:
    @staticmethod
    def get_all():
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM moradores")
        moradores = cursor.fetchall()
        return [Morador(*row) for row in moradores]

    @staticmethod
    def get_by_id(cpf):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM moradores WHERE cpf = %s", (cpf,))
        row = cursor.fetchone()
        if row:
            return Morador(*row)
        return None

    @staticmethod
    def create(morador):
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO moradores (cpf, nome, torre, andar, apartamento, email, telefone, moradorescol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (morador.cpf, morador.nome, morador.torre, morador.andar, morador.apartamento, morador.email, morador.telefone, morador.moradorescol))
        db.connection.commit()

    @staticmethod
    def update(morador):
        cursor = db.connection.cursor()
        cursor.execute("UPDATE moradores SET nome = %s, torre = %s, andar = %s, apartamento = %s, email = %s, telefone = %s, moradorescol = %s WHERE cpf = %s",
                       (morador.nome, morador.torre, morador.andar, morador.apartamento, morador.email, morador.telefone, morador.moradorescol, morador.cpf))
        db.connection.commit()

    @staticmethod
    def delete(cpf):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM moradores WHERE cpf = %s", (cpf,))
        db.connection.commit()
