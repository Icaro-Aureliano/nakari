from app.models.espaco import Espaco
from app import db

class EspacoRepository:
    @staticmethod
    def get_all():
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM espacos")
        espacos = cursor.fetchall()
        return [Espaco(*row) for row in espacos]

    @staticmethod
    def get_by_id(codigo):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM espacos WHERE codigo = %s", (codigo,))
        row = cursor.fetchone()
        if row:
            return Espaco(*row)
        return None

    @staticmethod
    def create(espaco):
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO espacos (nome, ds, status, capacidade) VALUES (%s, %s, %s, %s)",
                       (espaco.nome, espaco.ds, espaco.status, espaco.capacidade))
        db.connection.commit()
        espaco.codigo = cursor.lastrowid

    @staticmethod
    def update(espaco):
        cursor = db.connection.cursor()
        cursor.execute("UPDATE espacos SET nome = %s, ds = %s, status = %s, capacidade = %s WHERE codigo = %s",
                       (espaco.nome, espaco.ds, espaco.status, espaco.capacidade, espaco.codigo))
        db.connection.commit()

    @staticmethod
    def delete(codigo):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM espacos WHERE codigo = %s", (codigo,))
        db.connection.commit()
