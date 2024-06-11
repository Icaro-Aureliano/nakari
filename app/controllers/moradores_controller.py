from flask import Blueprint, render_template, request, redirect, url_for
from app.services.morador_service import MoradorService

moradores_bp = Blueprint('moradores', __name__, url_prefix='/moradores')

@moradores_bp.route('/')
def list_moradores():
    moradores = MoradorService.get_all_moradores()
    return render_template('list_moradores.html', moradores=moradores)

@moradores_bp.route('/<cpf>')
def view_morador(cpf):
    morador = MoradorService.get_morador_by_cpf(cpf)
    return render_template('view_morador.html', morador=morador)

@moradores_bp.route('/create', methods=['GET', 'POST'])
def create_morador():
    if request.method == 'POST':
        data = request.form.to_dict()
        MoradorService.create_morador(**data)
        return redirect(url_for('moradores.list_moradores'))
    return render_template('create_morador.html')

@moradores_bp.route('/update/<cpf>', methods=['GET', 'POST'])
def update_morador(cpf):
    if request.method == 'POST':
        data = request.form.to_dict()
        MoradorService.update_morador(**data)
        return redirect(url_for('moradores.list_moradores'))
    morador = MoradorService.get_morador_by_cpf(cpf)
    return render_template('update_morador.html', morador=morador)

@moradores_bp.route('/delete/<cpf>', methods=['GET','POST'])
def delete_morador(cpf):
    if request.method == 'POST':
        MoradorService.delete_morador(cpf)
        return redirect(url_for('moradores.list_moradores'))
    morador = MoradorService.get_morador_by_cpf(cpf)
    return render_template('delete_morador.html', morador=morador)