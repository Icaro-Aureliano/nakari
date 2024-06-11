from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    mysql.init_app(app)
    app.config['mysql'] = mysql

    from app.controllers.agendamento_controller import agendamento_bp
    from app.controllers.espaco_controller import espaco_bp
    from app.controllers.usuario_controller import usuario_bp
    from app.controllers.moradores_controller import moradores_bp
    from app.controllers.funcionarios_controller import funcionarios_bp
    from app.controllers.terceiros_controller import terceiros_bp
    from app.controllers.os_controller import os_bp

    app.register_blueprint(agendamento_bp)
    app.register_blueprint(espaco_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(moradores_bp)
    app.register_blueprint(funcionarios_bp)
    app.register_blueprint(terceiros_bp)
    app.register_blueprint(os_bp)

    return app
