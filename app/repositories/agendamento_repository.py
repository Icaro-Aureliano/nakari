from app.models.agendamento import Agendamento
from app import db

class AgendamentoRepository:
    @staticmethod
    def get_all():
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM agendamento")
        agendamentos = cursor.fetchall()
        return [Agendamento(*row) for row in agendamentos]

    @staticmethod
    def get_by_id(codigo):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM agendamento WHERE codigo = %s", (codigo,))
        row = cursor.fetchone()
        if row:
            return Agendamento(*row)
        return None

    @staticmethod
    def create(agendamento):
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (agendamento.data_emissao, agendamento.data_agendamento, agendamento.status, agendamento.hora_ini, agendamento.hora_fim, agendamento.moradores_cpf, agendamento.espacos_codigo))
        db.connection.commit()
        agendamento.codigo = cursor.lastrowid

    @staticmethod
    def update(agendamento):
        cursor = db.connection.cursor()
        cursor.execute("UPDATE agendamento SET data_emissao = %s, data_agendamento = %s, status = %s, hora_ini = %s, hora_fim = %s, moradores_cpf = %s, espacos_codigo = %s WHERE codigo = %s",
                       (agendamento.data_emissao, agendamento.data_agendamento, agendamento.status, agendamento.hora_ini, agendamento.hora_fim, agendamento.moradores_cpf, agendamento.espacos_codigo, agendamento.codigo))
        db.connection.commit()

    @staticmethod
    def delete(codigo):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM agendamento WHERE codigo = %s", (codigo,))
        db.connection.commit()
