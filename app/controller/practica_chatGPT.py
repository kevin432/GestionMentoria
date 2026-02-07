from flask import Blueprint, render_template
import re

practica_chatgpt = Blueprint('practica_chatgpt', __name__)

@practica_chatgpt.route("/saludo/<nombre>")
def saluar(nombre):
    
    return render_template('saluar.html', nombre = nombre)


@practica_chatgpt.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    result = a + b
    par = "PAR" if result % 2 == 0 else "IMPAR"
        
    return render_template("suma1.html", a = a, b = b, result = result, par = par)

@practica_chatgpt.route("/edad/<int:anio>")
def edad_anio(anio):
    edad = 0
    mayor = ""
    if anio >= 1920:
        edad = 2026 - anio
        if edad >= 19:
            mayor = "Es mayor de edad"
        else:
            mayor = "No es mayor de edad"
            
    else:
        edad = "El año debe ser mayor del año 1920"
        
    return render_template("edad.html", anio = anio, edad = edad, mayor = mayor)    
            