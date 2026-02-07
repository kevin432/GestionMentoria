from flask import Blueprint, render_template
import re

practica = Blueprint('practica', __name__)

@practica.route("/primera")
def home():
    return render_template("PrimeraPagina.html")

@practica.route("/Matriz/<int:n>")

def matriz(n):
    #Reto: Crea una ruta /matriz/<int:n> que genere una matriz de identidad de 
    # tamaño n * n usando comprensión de listas y la muestre en una tabla HTML.
    
    matriz_1 = [[1 if i == j else 0 for j in range(n)]for i in range(n)]
    
    return render_template("suma.html", matriz = matriz_1, n = n)

@practica.route("/CleanUp")

def clean_up():
    datos = [" luis perez", "MARTA gomez ", " ANa lopez "]
    
    datos_limpio = [i.strip().title() for i in datos]
    
    return render_template("CleanUp.html", datos = datos, datos_limpio =  datos_limpio)

@practica.route("/asistencia")
def Semáforo_Asistencia():
    asistencia = [['P', 'F', 'P'], ['P', 'P', 'P'], ['F', 'F', 'P']]
    
    return render_template("asistencia.html", asistencia = asistencia)

@practica.route("/Iva")

def iva():
    precios = [[10, 20], [30, 40]]
    precio_iva = [[(j * 0.15 + j) for j in i] for i in precios]
    
    return render_template('iva.html', precios = precios, precio_iva = precio_iva)

@practica.route("/Palabra")
def palabra_grande():
    cuento = """Hace mucho mucho tiempo, un niño paseaba por un prado en cuyo centro encontró un árbol con un cartel que decía: soy un árbol encantado, si dices las palabras mágicas, lo verás.

            El niño trató de acertar el hechizo, y probó con abracadabra, supercalifragilisticoespialidoso, tan-ta-ta-chán, y muchas otras, pero nada. Rendido, se tiró suplicante, diciendo: "¡¡por favor, arbolito!!", y entonces, se abrió una gran puerta en el árbol. Todo estaba oscuro, menos un cartel que decía: "sigue haciendo magia". Entonces el niño dijo "¡¡Gracias, arbolito!!", y se encendió dentro del árbol una luz que alumbraba un camino hacia una gran montaña de juguetes y chocolate.

    """
    import re

    cuento = re.sub(r'[,\."!?¡¿:]', '', cuento)

    palabaras_grandes = [palabra for palabra in cuento.split() if len(palabra) >= 5]
    
    return render_template('palabra.html', cuento = cuento, palabaras_grandes = palabaras_grandes)