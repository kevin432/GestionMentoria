// Espera a que todo el documento HTML esté completamente cargado
// antes de ejecutar cualquier código JavaScript
$(document).ready(function () {
  // Llama a la función que inicializa el formulario
  inicializarFormulario();
});

// --------------------------------------------------
// 1️⃣ Inicializa el evento submit del formulario
// --------------------------------------------------
function inicializarFormulario() {
  // Selecciona el formulario por su ID (#mensaje_nombre)
  // y escucha el evento "submit"
  $("#mensaje_nombre").on("submit", function (e) {
    // Evita que el formulario se envíe de forma tradicional
    // (evita recargar la página)
    e.preventDefault();

    // Obtiene los datos escritos en el formulario
    let datos = obtenerDatosFormulario();

    // Valida los datos antes de enviarlos al backend
    if (validarDatos(datos)) {
      // Si los datos son válidos, se envían al servidor
      enviarDatos(datos);
    }
  });
}

// --------------------------------------------------
// 2️⃣ Obtiene los datos del formulario
// --------------------------------------------------
function obtenerDatosFormulario() {
  // Retorna un objeto JavaScript con los valores del formulario
  return {
    // Obtiene el valor del input con id="nombre"
    // .trim() elimina espacios al inicio y al final
    nombre: $("#nombre").val().trim(),

    // Obtiene el valor del input o textarea con id="mensaje"
    mensaje: $("#mensaje").val().trim(),
  };
}

// --------------------------------------------------
// 3️⃣ Valida los datos del formulario
// --------------------------------------------------
function validarDatos(datos) {
  // Verifica si algún campo está vacío
  if (datos.nombre === "" || datos.mensaje === "") {
    alert("Todos los campos son obligatorios");
    return false; // Detiene el envío
  }

  // Si todas las validaciones pasan, retorna true
  return true;
}

// --------------------------------------------------
// 4️⃣ Envía los datos al backend usando AJAX
// --------------------------------------------------
function enviarDatos(datos) {
  // $.ajax permite hacer peticiones HTTP sin recargar la página
  $.ajax({
    // URL de la ruta en Flask
    url: "/mensaje",

    // Método HTTP
    type: "POST",

    // Indica que se enviarán datos en formato JSON
    contentType: "application/json",

    // Convierte el objeto JavaScript a JSON
    data: JSON.stringify(datos),

    // Se ejecuta si el servidor responde correctamente
    success: function (respuesta) {
      console.log("Respuesta del servidor:", respuesta);
    },

    // Se ejecuta si ocurre un error
    error: function () {
      console.error("Error al enviar datos");
    },
  });
}
