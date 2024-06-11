from flask import Blueprint, render_template, request, redirect, url_for
from app.services.terceiro_service import TerceiroService

terceiros_bp = Blueprint('terceiros', __name__, url_prefix='/terceiros')

@terceiros_bp.route('/')
def list_terceiros():
    terceiros = TerceiroService.get_all_terceiros()
    return render_template('list_terceiros.html', terceiros=terceiros)

@terceiros_bp.route('/<coc>')
def view_terceiro(coc):
    terceiro = TerceiroService.get_terceiro_by_coc(coc)
    return render_template('view_terceiro.html', terceiro=terceiro)

@terceiros_bp.route('/create', methods=['GET', 'POST'])
def create_terceiro():
    if request.method == 'POST':
        data = request.form.to_dict()
        TerceiroService.create_terceiro(**data)
        return redirect(url_for('terceiros.list_terceiros'))
    return render_template('create_terceiro.html')

@terceiros_bp.route('/update/<coc>', methods=['GET', 'POST'])
def update_terceiro(coc):
    if request.method == 'POST':
        data = request.form.to_dict()
        TerceiroService.update_terceiro(coc, data)
        return redirect(url_for('terceiros.list_terceiros'))
    terceiro = TerceiroService.get_terceiro_by_coc(coc)
    return render_template('update_terceiro.html', terceiro=terceiro)

@terceiros_bp.route('/delete/<coc>', methods=['GET','POST'])
def delete_terceiro(coc):
    if request.method == 'POST':
        TerceiroService.delete_terceiro(coc)
        return redirect(url_for('terceiros.list_terceiros'))
    terceiro = TerceiroService.get_terceiro_by_coc(coc)
    return render_template('delete_terceiro.html', terceiro=terceiro)