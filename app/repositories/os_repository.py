from app.models.os import Os
from app import db

class OsRepository:
    @staticmethod
    def get_all():
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM os")
        os_list = cursor.fetchall()
        return [Os(*row) for row in os_list]

    @staticmethod
    def get_by_id(codigo):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM os WHERE codigo = %s", (codigo,))
        row = cursor.fetchone()
        if row:
            return Os(*row)
        return None

    @staticmethod
    def create(os):
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (os.servico, os.ds, os.prioridade, os.status, os.tempo, os.modalidade, os.preco, os.prestador_nom, os.prestador_coc, os.obs, os.apartamento, os.moradores_cpf, os.funcionarios_cpf, os.terceiros_coc))
        db.connection.commit()

    @staticmethod
    def update(os):
        cursor = db.connection.cursor()
        cursor.execute("UPDATE os SET servico = %s, ds = %s, prioridade = %s, status = %s, tempo = %s, modalidade = %s, preco = %s, prestador_nom = %s, prestador_coc = %s, obs = %s, apartamento = %s, moradores_cpf = %s, funcionarios_cpf = %s, terceiros_coc = %s WHERE codigo = %s",
                       (os.servico, os.ds, os.prioridade, os.status, os.tempo, os.modalidade, os.preco, os.prestador_nom, os.prestador_coc, os.obs, os.apartamento, os.moradores_cpf, os.funcionarios_cpf, os.terceiros_coc, os.codigo))
        db.connection.commit()

    @staticmethod
    def delete(codigo):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM os WHERE codigo = %s", (codigo,))
        db.connection.commit()
