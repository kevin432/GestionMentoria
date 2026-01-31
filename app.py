from flask import Flask

app = Flask(__name__)

@app.route("/")

def hola_mundo():
    return "HOLA MUNDO KEVIN"

if __name__ == "__main__":
    app.run()