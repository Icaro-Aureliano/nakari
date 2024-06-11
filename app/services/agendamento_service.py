from flask import current_app

class AgendamentoService:
    @staticmethod
    def get_all_agendamentos():
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM agendamento")
        agendamentos = cursor.fetchall()
        cursor.close()
        return agendamentos
    
    @staticmethod
    def get_agendamento_by_id(codigo):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM agendamento WHERE codigo = %s", (codigo,))
        agendamento = cursor.fetchone()
        cursor.close()
        return agendamento
    
    @staticmethod
    def create_agendamento(**data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (data['data_emissao'], data['data_agendamento'], data['status'], data['hora_ini'], data['hora_fim'], data['moradores_cpf'], data['espacos_codigo']))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def update_agendamento(codigo, **data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "UPDATE agendamento SET data_emissao=%s, data_agendamento=%s, status=%s, hora_ini=%s, hora_fim=%s, moradores_cpf=%s, espacos_codigo=%s WHERE codigo=%s"
        cursor.execute(query, (data['data_emissao'], data['data_agendamento'], data['status'], data['hora_ini'], data['hora_fim'], data['moradores_cpf'], data['espacos_codigo'], codigo))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def delete_agendamento(codigo):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM agendamento WHERE codigo = %s", (codigo,))
        db.connection.commit()
        cursor.close()
