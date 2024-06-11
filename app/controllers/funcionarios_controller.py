from flask import Blueprint, render_template, request, redirect, url_for
from app.services.funcionario_service import FuncionarioService

funcionarios_bp = Blueprint('funcionarios', __name__, url_prefix='/funcionarios')

@funcionarios_bp.route('/')
def list_funcionarios():
    funcionarios = FuncionarioService.get_all_funcionarios()
    return render_template('list_funcionarios.html', funcionarios=funcionarios)

@funcionarios_bp.route('/<cpf>')
def view_funcionario(cpf):
    funcionario = FuncionarioService.get_funcionario_by_cpf(cpf)
    return render_template('view_funcionario.html', funcionario=funcionario)

@funcionarios_bp.route('/create', methods=['GET', 'POST'])
def create_funcionario():
    if request.method == 'POST':
        data = request.form.to_dict()
        FuncionarioService.create_funcionario(**data)
        return redirect(url_for('funcionarios.list_funcionarios'))
    return render_template('create_funcionario.html')

@funcionarios_bp.route('/update/<cpf>', methods=['GET', 'POST'])
def update_funcionario(cpf):
    if request.method == 'POST':
        data = request.form.to_dict()
        FuncionarioService.update_funcionario(**data)
        return redirect(url_for('funcionarios.list_funcionarios'))
    funcionario = FuncionarioService.get_funcionario_by_cpf(cpf)
    return render_template('update_funcionario.html', funcionario=funcionario)

@funcionarios_bp.route('/delete/<cpf>', methods=['GET','POST'])
def delete_funcionario(cpf):
    if request.method == 'POST':
        FuncionarioService.delete_funcionario(cpf)
        return redirect(url_for('funcionarios.list_funcionarios'))
    funcionario = FuncionarioService.get_funcionario_by_cpf(cpf)
    return render_template('delete_funcionario.html', funcionario=funcionario)