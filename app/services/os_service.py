from flask import current_app

class OSService:
    @staticmethod
    def get_all_os():
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM os")
        ordens = cursor.fetchall()
        cursor.close()
        return ordens
    
    @staticmethod
    def get_os_by_id(codigo):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM os WHERE codigo = %s", (codigo,))
        ordem = cursor.fetchone()
        cursor.close()
        return ordem
    
    @staticmethod
    def create_os(**data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(
            query, 
            (data['servico'], 
             data['ds'], 
             data['prioridade'], 
             data['status'], 
             data['tempo'], 
             data['modalidade'], 
             data['preco'], 
             data['prestador_nom'], 
             data['prestador_coc'], 
             data['obs'], 
             data['apartamento'], 
             data['moradores_cpf'], 
             data['funcionarios_cpf'], 
             data['terceiros_coc']
            ))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def update_os(codigo, **data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "UPDATE os SET servico=%s, ds=%s, prioridade=%s, status=%s, tempo=%s, modalidade=%s, preco=%s, prestador_nom=%s, prestador_coc=%s, obs=%s, apartamento=%s, moradores_cpf=%s, funcionarios_cpf=%s, terceiros_coc=%s WHERE codigo=%s"
        cursor.execute(
            query, 
            (data['servico'], 
             data['ds'], 
             data['prioridade'], 
             data['status'], 
             data['tempo'], 
             data['modalidade'], 
             data['preco'], 
             data['prestador_nom'], 
             data['prestador_coc'], 
             data['obs'], 
             data['apartamento'], 
             data['moradores_cpf'], 
             data['funcionarios_cpf'], 
             data['terceiros_coc'], 
             codigo
            ))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def delete_os(codigo):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM os WHERE codigo = %s", (codigo,))
        db.connection.commit()
        cursor.close()
