# Este é o código do servidor/backend do sistema, que intermedia as comunicações entre o usuário
# final na interface gráfica e o robô/microcontrolador. Essas comunicações se dão através de diferentes
# rotas de leitura e mudança de estados, que alteram variáveis globais e executam funções específicas
# em cada subsistema.

from flask import Flask, request
from flask_cors import CORS  # módulo para evitar erros de CORS
from magnetum.config import db
from magnetum.blueprints import routes

def create_app():
    app = Flask(__name__)  # Cria servidor
    db
    CORS(app)  # Adiciona proteção contra erros CORS
    routes.init_app(app)
    return app