from app.models.funcionario import Funcionario
from app import db

class FuncionarioRepository:
    @staticmethod
    def get_all():
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()
        return [Funcionario(*row) for row in funcionarios]

    @staticmethod
    def get_by_id(cpf):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM funcionarios WHERE cpf = %s", (cpf,))
        row = cursor.fetchone()
        if row:
            return Funcionario(*row)
        return None

    @staticmethod
    def create(funcionario):
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO funcionarios (cpf, nome, endereco, admissao, rg, salario) VALUES (%s, %s, %s, %s, %s, %s)",
                       (funcionario.cpf, funcionario.nome, funcionario.endereco, funcionario.admissao, funcionario.rg, funcionario.salario))
        db.connection.commit()

    @staticmethod
    def update(funcionario):
        cursor = db.connection.cursor()
        cursor.execute("UPDATE funcionarios SET nome = %s, endereco = %s, admissao = %s, rg = %s, salario = %s WHERE cpf = %s",
                       (funcionario.nome, funcionario.endereco, funcionario.admissao, funcionario.rg, funcionario.salario, funcionario.cpf))
        db.connection.commit()

    @staticmethod
    def delete(cpf):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE cpf = %s", (cpf,))
        db.connection.commit()
