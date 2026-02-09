from flask import Blueprint, render_template
import re

practica_2 = Blueprint('practica_2', __name__)

@practica_2.route("/Perfil")
def perfil():
    data = {
    "nombre": "Kevin Terán",
    "edad": 20,
    "carrera": "Desarrollo de Software"
}
    return render_template("perfil.html", **data)

@practica_2.route("/producto")
def producto():
    desc = 0.12
    productos = {
        "nombre": "Laptop",
        "precio": 800,
        "stock": 5,
        "descuento": 0
    }
    
    productos["descuento"]= round(productos["precio"] - productos["precio"] * desc , 2)
    
    return render_template("producto.html", **productos)

@practica_2.route("/estudiantes")
def estudiantes():
    estudiantes = [
        {"nombre": "Ana", "materia": "Matematicas","nota": 9},
        {"nombre": "Luis", "materia": "Historia","nota": 7},
        {"nombre": "Carlos", "materia": "Lengua y Literatura","nota": 5}
    ]
    return render_template("estudiante.html", estudiantes=estudiantes)
