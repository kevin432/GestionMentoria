from flask import Flask, Blueprint, request, render_template, redirect
from pymongo import MongoClient

mongo = Blueprint("mongo", __name__)

cliente = MongoClient("mongodb+srv://kevinteran750:HROXM4YkWO8cCcKl@pruebas.llgoe.mongodb.net/")
db = cliente["libreria"]        # nombre de la base de datos
#coleccion = db["usuarios"]     # nombre de la colección
coleccion = db["producto"]

@mongo.route("/UsuarioM", methods=["GET", "POST"])
def usuario_m():
    #Verifica si los datos son enviados por post
    if request.method == "POST":
        #Obtiene los valores del formulario 
        nombre = request.form.get("nombre")
        edad = request.form.get("edad")
        
        #Verifica si nombre y edad no esta vacio, si edad es un digito numerico
        if nombre and nombre.strip() and edad and edad.isdigit():
    
            #guarda la edad parseandolo antes
            edad_int = int(edad)

            #verifica si la edad sean numeros entre el 5 al 100
            if 5 <= edad_int <= 100:
                #Crea un Diccionario con los datos
                usuario = {
                    "nombre": nombre.strip(),
                    "edad": edad_int
                }

                #Guarda los datos en MongoDB
                coleccion.insert_one(usuario)
                
                #Redirecciona
                return redirect("/UsuarioM")
    
    #Guardo la data de la BD en una variable   
    usuarios = list(coleccion.find())
    print(usuarios)
    
    #retorna la pagina (html), y los datos de la DB para consumirlas en la web
    return render_template("usuario1.html", usuarios = usuarios)

@mongo.route("/productoM", methods=["GET", "POST"])
def producto_m():
    
    if request.method == "POST":
        nombre = request.form.get("nombre").strip()
        precio = float(request.form.get("precio"))
        stock = int(request.form.get("stock"))
        
        validar = nombre != "" and precio >= 0.0 and stock >= 0
        
        if validar:
            producto = {
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            }
            
            coleccion.insert_one(producto)
            redirect("productoM")
            
    productos = list(coleccion.find())
    
    return render_template("productoM.html", productos = productos)