from flask import Flask, Blueprint, render_template, request
from datetime import datetime, timedelta
from pymongo import MongoClient

semana_3 = Blueprint("semana_3", __name__)

#CLIENTE PARA CONECTAR MONGODB
cliente = MongoClient("mongodb+srv://kevinteran750:HROXM4YkWO8cCcKl@pruebas.llgoe.mongodb.net/")

def obtener_fecha_actual():
    fecha_actual = datetime.now()

    # Ir al primer día del mes actual
    primer_dia_mes_actual = fecha_actual.replace(day=1)

    # Restar 1 día → último día del mes anterior
    ultimo_dia_mes_anterior = primer_dia_mes_actual - timedelta(days=1)

    return {
        "anio": fecha_actual.year,
        "mes": fecha_actual.month,
        "dia": fecha_actual.day,
        "ultimo_dia_mes_anterior_anio": ultimo_dia_mes_anterior.year,
        "ultimo_dia_mes_anterior_mes": ultimo_dia_mes_anterior.month,
        "ultimo_dia_mes_anterior_dia": ultimo_dia_mes_anterior.day
    }


@semana_3.route("/Par", methods = ["GET", "POST"])
def par():
    
    numero = 0
    par = ""
    if request.method == "POST":
        numero = int(request.form.get("numero"))
        
    if numero % 2 == 0:
        par = f"El número {numero} es par"
    else:
        par = f"El número {numero} es impar"
        

    return render_template("Par.html", par = par)

@semana_3.route("/Calcular-edad", methods = ["GET", "POST"])
def calcular_edad():
    fecha = obtener_fecha_actual()
    edad = 0
    anio = 0
    anio_actual = fecha["anio"]
    
    if request.method == "POST":
        anio = int(request.form.get("anio"))
        edad = anio_actual - anio
    
    print(edad)
    return render_template("calcularEdad.html", edad=edad)

@semana_3.route("/edad", methods = ["GET", "POST"])
def edad2():
    fecha = obtener_fecha_actual()
    anio_acual = fecha["anio"]
    mes_actual = fecha["mes"]
    dia_actual = fecha["dia"]
     
    anio = 0
    mes = 0
    dia = 0

    edad_anio = 0
    edad_mes = 0
    edad_dia = 0
    
    if request.method == "POST":
        try:
            anio = int(request.form.get("anio"))
            mes = int(request.form.get("mes"))
            dia = int(request.form.get("dia"))
            
            edad_anio = int(anio_acual) - anio 
            edad_mes = int(mes_actual) - mes
            edad_dia = int(dia_actual) - dia
        
        
            if edad_dia < 0:
                edad_mes -= 1
                
                edad_dia += fecha["ultimo_dia_mes_anterior_dia"]
                
            if edad_mes < 0:
                edad_anio -= 1
                
                edad_mes += 12
    
        except (TypeError, ValueError):
            edad_anio = edad_mes = edad_dia = "Fecha inválida"

    return render_template("calcularEdad2.html", edad_anio = edad_anio, edad_mes = edad_mes, edad_dia = edad_dia)
        

    