from flask import Blueprint, render_template, request, redirect, url_for
from app.services.os_service import OSService

os_bp = Blueprint('os', __name__, url_prefix='/os')

@os_bp.route('/')
def list_os():
    os_list = OSService.get_all_os()
    return render_template('list_os.html', os_list=os_list)

@os_bp.route('/<int:codigo>')
def view_os(codigo):
    os = OSService.get_os_by_id(codigo)
    return render_template('view_os.html', ordem=os)

@os_bp.route('/create', methods=['GET', 'POST'])
def create_os():
    if request.method == 'POST':
        data = request.form.to_dict()
        OSService.create_os(**data)
        return redirect(url_for('os.list_os'))
    return render_template('create_os.html')

@os_bp.route('/update/<int:codigo>', methods=['GET', 'POST'])
def update_os(codigo):
    if request.method == 'POST':
        data = request.form.to_dict()
        OSService.update_os(codigo, **data)
        return redirect(url_for('os.list_os'))
    os = OSService.get_os_by_id(codigo)
    return render_template('update_os.html', ordem=os)

@os_bp.route('/delete/<int:codigo>', methods=['GET','POST'])
def delete_os(codigo):
    if request.method == 'POST':
        OSService.delete_os(codigo)
        return redirect(url_for('os.list_os'))
    os = OSService.get_os_by_id(codigo)
    print(os)
    return render_template('delete_os.html', ordem=os)