from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar y registrar controladores (Blueprints)
    from app.controller.practica import practica
    app.register_blueprint(practica)
    
    # Importar y registrar controladores (Blueprints)
    from app.controller.practica_chatGPT import practica_chatgpt
    app.register_blueprint(practica_chatgpt)

    return app
