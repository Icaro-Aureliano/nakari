from flask import current_app

class FuncionarioService:
    @staticmethod
    def get_all_funcionarios():
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()
        cursor.close()
        return funcionarios
    
    @staticmethod
    def get_funcionario_by_cpf(cpf):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM funcionarios WHERE cpf = %s", (cpf,))
        funcionario = cursor.fetchone()
        cursor.close()
        return funcionario
    
    @staticmethod
    def create_funcionario(**data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        query = "INSERT INTO funcionarios (cpf, nome, rg, endereco, salario, admissao) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (data['cpf'], data['nome'], data['rg'], data['endereco'], data['salario'], data['admissao']))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def update_funcionario(cpf, **data):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        print(data)
        query = "UPDATE funcionarios SET nome=%s, salario=%s, admissao=%s, endereco=%s, rg=%s WHERE cpf=%s"
        cursor.execute(query, (data['nome'], data['salario'], data['admissao'], data['endereco'], data['rg'], cpf))
        db.connection.commit()
        cursor.close()
    
    @staticmethod
    def delete_funcionario(cpf):
        db = current_app.config['mysql']
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE cpf = %s", (cpf,))
        db.connection.commit()
        cursor.close()
