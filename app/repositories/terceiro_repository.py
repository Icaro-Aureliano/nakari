from app.models.terceiro import Terceiro
from app import db

class TerceiroRepository:
    @staticmethod
    def get_all():
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM terceiros")
        terceiros = cursor.fetchall()
        return [Terceiro(*row) for row in terceiros]

    @staticmethod
    def get_by_id(coc):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM terceiros WHERE coc = %s", (coc,))
        row = cursor.fetchone()
        if row:
            return Terceiro(*row)
        return None

    @staticmethod
    def create(terceiro):
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO terceiros (coc, razao, endereco, preco, servico, status, email, telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (terceiro.coc, terceiro.razao, terceiro.endereco, terceiro.preco, terceiro.servico, terceiro.status, terceiro.email, terceiro.telefone))
        db.connection.commit()

    @staticmethod
    def update(terceiro):
        cursor = db.connection.cursor()
        cursor.execute("UPDATE terceiros SET razao = %s, endereco = %s, preco = %s, servico = %s, status = %s, email = %s, telefone = %s WHERE coc = %s",
                       (terceiro.razao, terceiro.endereco, terceiro.preco, terceiro.servico, terceiro.status, terceiro.email, terceiro.telefone, terceiro.coc))
        db.connection.commit()

    @staticmethod
    def delete(coc):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM terceiros WHERE coc = %s", (coc,))
        db.connection.commit()
