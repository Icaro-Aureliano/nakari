from flask import Blueprint, render_template, request, redirect, url_for
from app.services.agendamento_service import AgendamentoService

agendamento_bp = Blueprint('agendamento', __name__, url_prefix='/agendamentos')

@agendamento_bp.route('/')
def list_agendamentos():
    agendamentos = AgendamentoService.get_all_agendamentos()
    return render_template('list_agendamentos.html', agendamentos=agendamentos)

@agendamento_bp.route('/<int:codigo>')
def view_agendamento(codigo):
    agendamento = AgendamentoService.get_agendamento_by_id(codigo)
    return render_template('view_agendamento.html', agendamento=agendamento)

@agendamento_bp.route('/create', methods=['GET', 'POST'])
def create_agendamento():
    if request.method == 'POST':
        data = request.form.to_dict()
        AgendamentoService.create_agendamento(**data)
        return redirect(url_for('agendamento.list_agendamentos'))
    return render_template('create_agendamento.html')

@agendamento_bp.route('/update/<int:codigo>', methods=['GET', 'POST'])
def update_agendamento(codigo):
    if request.method == 'POST':
        data = request.form.to_dict()
        AgendamentoService.update_agendamento(codigo, **data)
        return redirect(url_for('agendamento.list_agendamentos'))
    agendamento = AgendamentoService.get_agendamento_by_id(codigo)
    return render_template('update_agendamento.html', agendamento=agendamento)

@agendamento_bp.route('/delete/<int:codigo>', methods=['GET','POST'])
def delete_agendamento(codigo):
    if request.method == 'POST':
        AgendamentoService.delete_agendamento(codigo)
        return redirect(url_for('agendamento.list_agendamentos'))
    agendamento = AgendamentoService.get_agendamento_by_id(codigo)
    return render_template('delete_agendamento.html', agendamento=agendamento)
