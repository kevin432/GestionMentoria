from flask import Blueprint, render_template, request, jsonify

primera_pagina = Blueprint('primera_pagina', __name__)

#Mediante la ruta /primerapagina mostrar el archivo primerapagina.html 
@primera_pagina.route("/primerapagina", methods=["GET"])
def index():
    return render_template("primerapagina.html")

@primera_pagina.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.get_json()
    
    nombre = data.get("nombre")
    mensaje = data.get("mensaje")
    
    print("Nuevo mensaje recibio")
    print(f"Nombre: {nombre}")
    print(f"Mensaje: {mensaje}")
    
    return jsonify({
        "success": True,
        "msg": "Datos enviaos correctamente"
    })
    
    
@primera_pagina.route("/crear_usuario", methods=["GET"])
def crearUser():
    return render_template("crearUsuario.html") 

@primera_pagina.route("/crear", methods=["POST"])
def usuario():
    data = request.get_json()
    
    nombre = data.get("nombre")
    email = data.get("email")
    password = data.get("password")
    
    print("Usuario creado correctamente")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Contraseña: {password}")
    
    return jsonify({
        "success": True,
        "msg": "SI FUNCIONA CULERO"
    })
    
@primera_pagina.route("/estudiante", methods=["GET"])
def estudiante():
    return render_template("notas.html")

@primera_pagina.route("/guardarnotas", methods=["POST"])
def guardar_notas():
    datos = request.get_json()
    
    nombre = datos.get("nombre")
    materia = datos.get("materia")
    nota = datos.get("nota")
    
    print("SUS NOTAS SON:")
    print(f"Nombre del estudiante: {nombre}")
    print(f"Materia: {materia}")
    print(f"Nota: {nota}")
    
    return jsonify({
        "success": True,
        "msg": "SI FUNCIONA JAJA"
    })
    
    