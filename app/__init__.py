from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.controller.primeraPagina import primera_pagina
    app.register_blueprint(primera_pagina)
    
    from app.controller.loop import loop
    app.register_blueprint(loop)
    
    return app