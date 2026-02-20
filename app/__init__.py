from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.controller.semana_2.primeraPagina import primera_pagina
    app.register_blueprint(primera_pagina)
    
    from app.controller.semana_2.loop import loop
    app.register_blueprint(loop)
    
    from app.controller.Semana_3.semana_3 import semana_3
    app.register_blueprint(semana_3)
    
    from app.controller.Semana_3.mongoDB import mongo
    app.register_blueprint(mongo)
    
    return app