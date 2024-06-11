from flask import Blueprint, render_template, request, redirect, url_for
from app.services.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario_bp.route('/')
def list_usuarios():
    usuarios = UsuarioService.get_all_usuarios()
    return render_template('list_usuarios.html', usuarios=usuarios)

@usuario_bp.route('/<cpf>')
def view_usuario(cpf):
    usuario = UsuarioService.get_usuario_by_cpf(cpf)
    return render_template('view_usuario.html', usuario=usuario)

@usuario_bp.route('/create', methods=['GET', 'POST'])
def create_usuario():
    if request.method == 'POST':
        data = request.form.to_dict()
        UsuarioService.create_usuario(**data)
        return redirect(url_for('usuario.list_usuarios'))
    return render_template('create_usuario.html')

@usuario_bp.route('/update/<cpf>', methods=['GET', 'POST'])
def update_usuario(cpf):
    if request.method == 'POST':
        data = request.form.to_dict()
        UsuarioService.update_usuario(**data)
        return redirect(url_for('usuario.list_usuarios'))
    usuario = UsuarioService.get_usuario_by_cpf(cpf)
    return render_template('update_usuario.html', usuario=usuario)

@usuario_bp.route('/delete/<cpf>', methods=['GET','POST'])
def delete_usuario(cpf):
    if request.method == 'POST':
        UsuarioService.delete_usuario(cpf)
        return redirect(url_for('usuario.list_usuarios'))
    usuario = UsuarioService.get_usuario_by_cpf(cpf)
    return render_template('delete_usuario.html', usuario=usuario)