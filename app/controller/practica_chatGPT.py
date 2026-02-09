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
    con_anio = 2026
    if anio >= 1920 and anio <= con_anio:
        edad = con_anio - anio
        if edad >= 19:
            mayor = "Es mayor de edad"
        else:
            mayor = "No es mayor de edad"
            
    else:
        edad = "El año debe ser mayor del año 1920 y menor al año actual 2026"
        
    return render_template("edad.html", anio = anio, edad = edad, mayor = mayor)    
            
            
@practica_chatgpt.route("/palabras/<palabra>")
def palabras(palabra):
    palabra = re.sub(r'[,\."!?¡¿:]', '', palabra)
    lista = [i for i in palabra.split() if len(i) >= 5 ]
    
    return render_template("palabra1.html", lista = lista)        

@practica_chatgpt.route("/TablaMultiplicar/<int:n>")
def tabla_multiplicar(n):

    resultados = []
    
    for i in range(11):
        resultados.append({
            "Multiplicador" : i,
            "Resultado": i * n
        })
    return render_template("TablaMultiplicar.html", n = n, resultados = resultados)

@practica_chatgpt.route("/nota")
def nota():
    notas = {"Matematica": 8.7, "Lengua y Literatura": 7.4, "Hitoria": 9.8, "Emprendimiento": 6.5}
    
    promedio = 0
    nota_alta = -1  # Inicializa con un valor muy bajo
    nota_baja = 20    # Inicializa con un valor muy alto
    cont = 0
    total = 0
    for nota in notas.values():
        cont += 1
        total += nota
        if nota > nota_alta:
            nota_alta = nota 
        if nota < nota_baja:
            nota_baja = nota
            
    prome = total / cont
    promedio = round(prome, 2)
    
    return render_template("Nota.html", promedio = promedio, nota_baja = nota_baja, nota_alta = nota_alta, notas = notas)

@practica_chatgpt.route("/matriz/<int:n>")
def matriz(n):
    matriz_n = [[1 if j==i else 0 for j in range(n)] for i in range(n)]
    
    return render_template("matriz.html", matriz_n = matriz_n)

@practica_chatgpt.route("/iva/<int:n>")
def iva(n):
    precio = [54, 74.5, 98, 157, 150.6, 70]
    
    iva_n = n/100 if n < 100 else "Ingrese el iva menor a 100"
    
    precio_iva = [round(i * iva_n + i, 2) for i in precio]
    
    iva_pagar = [round(i * iva_n, 2)  for i in precio]
    
    return render_template("Iva1.html", precio = precio, iva_n = iva_n, precio_iva = precio_iva, n = n, iva_pagar = iva_pagar)
    

@practica_chatgpt.route("/resumen")
def resumen():
    cuento = """Hace mucho mucho tiempo, un niño paseaba por un prado en cuyo centro encontró un árbol con un cartel que decía: soy un árbol encantado, si dices las palabras mágicas, lo verás.

            El niño trató de acertar el hechizo, y probó con abracadabra, supercalifragilisticoespialidoso, tan-ta-ta-chán, y muchas otras, pero nada. Rendido, se tiró suplicante, diciendo: "¡¡por favor, arbolito!!", y entonces, se abrió una gran puerta en el árbol. Todo estaba oscuro, menos un cartel que decía: "sigue haciendo magia". Entonces el niño dijo "¡¡Gracias, arbolito!!", y se encendió dentro del árbol una luz que alumbraba un camino hacia una gran montaña de juguetes y chocolate.
    """
    
    cuento = re.sub(r'[,\."!?¡¿:]', '', cuento)
    
    total_palabra = 0
    unica_palabra = {}
    unica_palabra_total = 0
    palabra_grande = []
    palabra_grande_total = 0
    
    for i in cuento.lower().split():
        total_palabra += 1
        
        unica_palabra[i] = unica_palabra.get(i, 0) + 1
            
        if len(i) >= 7:
            palabra_grande_total += 1
            palabra_grande.append(i)
            
    palabra_unica = []
    
    for palabra, total in unica_palabra.items():
        if total == 1:
            unica_palabra_total += 1
            palabra_unica.append(palabra)
        
            
    return render_template('Resumen.html', palabra_unica = palabra_unica,palabra_grande_total =  palabra_grande_total,total_palabra = total_palabra, unica_palabra = unica_palabra, palabra_grande = palabra_grande, cuento = cuento, unica_palabra_total = unica_palabra_total)
    
    
    