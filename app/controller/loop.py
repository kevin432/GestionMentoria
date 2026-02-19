from flask import Blueprint, Flask, render_template

loop = Blueprint("loop",__name__)

@loop.route("/numero")
def numeros():
    lista = [1, 2, 3, 4, 5]
    return render_template("ejemplo1.html", lista = lista)


@loop.route("/Multiplicar/<int:n>")

def mult(n):
    
    return render_template("Multiplicar.html", n = n)


@loop.route("/usuario")
def usuario():
    usuarios = ["Kevin", "Maria", "Luis"]
    tam_usu = len(usuarios) 
    return render_template("Usuario.html", usuarios = usuarios, tam_usu = tam_usu)

@loop.route("/Usuario-Lista")
def usu_lis():
    usuarios = [
    {"nombre": "Kevin", "edad": 20},
    {"nombre": "Maria", "edad": 22},
    {"nombre": "Luis", "edad": 28},
    {"nombre": "Sofía", "edad": 25},
    {"nombre": "Andrés", "edad": 30},
    {"nombre": "Valentina", "edad": 27},
    {"nombre": "Javier", "edad": 24},
    {"nombre": "Camila", "edad": 19},
    {"nombre": "Diego", "edad": 33},
    {"nombre": "Isabella", "edad": 21}
]

    edad_usu = [i for i in usuarios if i["edad"] > 21]
    
    return render_template("UsuList.html", usuarios = usuarios, edad_usu  = edad_usu )

@loop.route("/producto")
def producto():
    productos = [
    {"nombre": "Mouse", "precio": 15},
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 150},
    {"nombre": "Impresora", "precio": 85},
    {"nombre": "Laptop", "precio": 800},
    {"nombre": "Auriculares", "precio": 40},
    {"nombre": "Cámara Web", "precio": 60},
    {"nombre": "Disco Duro Externo", "precio": 100},
    {"nombre": "Router", "precio": 50},
    {"nombre": "Pendrive", "precio": 20}
]

    return render_template("proucto.html",  productos = productos)

@loop.route("/curso")
def curso():
    cursos = {
    "Backend": ["Flask", "Django", "Node.js", "Ruby on Rails"],
    "Frontend": ["HTML", "CSS", "JS", "React", "Vue.js"],
    "DevOps": ["Docker", "Kubernetes", "AWS", "Azure"],
    "Data Science": ["Python", "R", "Pandas", "Machine Learning"],
    "Mobile Development": ["React Native", "Flutter", "Swift", "Kotlin"]
}

    return render_template("Curso.html", cursos = cursos)

@loop.route("/Provincia")
def provincia():
    provincias_ecuador = [
    "Azuay",
    "Bolívar",
    "Cañar",
    "Carchi",
    "Chimborazo",
    "Cotopaxi",
    "El Oro",
    "Esmeraldas",
    "Galápagos",
    "Guayas",
    "Imbabura",
    "Loja",
    "Los Ríos",
    "Manabí",
    "Morona Santiago",
    "Napo",
    "Orellana",
    "Pastaza",
    "Pichincha",
    "Santa Elena",
    "Santo Domingo de los Tsáchilas",
    "Sucumbíos",
    "Tungurahua",
    "Zamora-Chinchipe"
]

    return render_template("Provincia.html", provincias_ecuador = provincias_ecuador)

@loop.route("/Nota")
def nota():
    # Lista de diccionarios con información de estudiantes
    estudiantes = [
        {
            "Nombre": "Juan Pérez",
            "Matematica": 8.5,
            "Lenguaje": 9.0,
            "Historia": 7.8,
            "Fisica": 8.8
        },
        {
            "Nombre": "Ana Gómez",
            "Matematica": 9.2,
            "Lenguaje": 9.5,
            "Historia": 8.9,
            "Fisica": 9.4
        },
        {
            "Nombre": "Luis Martínez",
            "Matematica": 7.6,
            "Lenguaje": 5.0,
            "Historia": 7.5,
            "Fisica": 6.2
        },
        {
            "Nombre": "Carla Ruiz",
            "Matematica": 8.8,
            "Lenguaje": 9.1,
            "Historia": 9.0,
            "Fisica": 8.7
        }
    ]

    promedio = []
    return render_template("Nota.html", estudiantes = estudiantes)

@loop.route("/carrito")
def carrito():
    productos= [
    {"producto": "Monitor", "precio": 150, "cantidad": 3},
    {"producto": "Laptop", "precio": 800, "cantidad": 1},
    {"producto": "Impresora", "precio": 100, "cantidad": 1},
    {"producto": "Altavoces", "precio": 50, "cantidad": 2},
    {"producto": "Webcam", "precio": 40, "cantidad": 4},
    {"producto": "Auriculares", "precio": 30, "cantidad": 1}
]
    total = 0
    
    for i in productos:
        total += i["precio"] * i["cantidad"]
    
    return render_template("Carrito.html", productos = productos, total = total)