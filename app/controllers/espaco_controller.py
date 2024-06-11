from flask import Blueprint, render_template, request, redirect, url_for, current_app
from app.services.espaco_service import EspacoService

espaco_bp = Blueprint('espaco', __name__, url_prefix='/espacos')

@espaco_bp.route('/')
def list_espacos():
    espacos = EspacoService.get_all_espacos()
    return render_template('list_espacos.html', espacos=espacos)

@espaco_bp.route('/<int:codigo>')
def view_espaco(codigo):
    espaco = EspacoService.get_espaco_by_id(codigo)
    return render_template('view_espaco.html', espaco=espaco)

@espaco_bp.route('/create', methods=['GET', 'POST'])
def create_espaco():
    if request.method == 'POST':
        data = request.form.to_dict()
        EspacoService.create_espaco(**data)
        return redirect(url_for('espaco.list_espacos'))
    return render_template('create_espaco.html')

@espaco_bp.route('/update/<int:codigo>', methods=['GET', 'POST'])
def update_espaco(codigo):
    if request.method == 'POST':
        data = request.form.to_dict()
        EspacoService.update_espaco(codigo, **data)
        return redirect(url_for('espaco.list_espacos'))
    espaco = EspacoService.get_espaco_by_id(codigo)
    return render_template('update_espaco.html', espaco=espaco)

@espaco_bp.route('/delete/<int:codigo>', methods=['GET','POST'])
def delete_espaco(codigo):
    if request.method == 'POST':
        EspacoService.delete_espaco(codigo)
        return redirect(url_for('espaco.list_espacos'))
    espaco = EspacoService.get_espaco_by_id(codigo)
    return render_template('delete_espaco.html', espaco=espaco)