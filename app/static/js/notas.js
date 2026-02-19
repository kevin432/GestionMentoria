//Funcion donde espera que el ocumento HTML este cargado
//para poder ejecutar un codigo
$(document).ready(function () {
  iniciarFormulario();
});

function iniciarFormulario() {
  $("#estudianteForm").on("submit", function (e) {
    e.preventDefault();

    let datos = obtenerDatos();

    if (validarDatos(datos)) {
      enviarDatos(datos);
    }
  });
}

function obtenerDatos() {
  return {
    nombre: $("#estudiante").val().trim(),
    materia: $("#materia").val().trim(),
    nota: $("#nota").val().trim(),
  };
}

function validarDatos(datos) {
  if (
    datos.nombre === "" ||
    datos.materia === "" ) {
    alert("Todos los datos deben estar llenos");
    return false;
  }

  return true;
}

function enviarDatos(datos) {
    console.log(datos)
  $.ajax({
    type: "POST",
    url: "/guardarnotas",
    data: JSON.stringify(datos),
    contentType: "application/json",
    success: function (response) {
      console.log("Respuesta del servidor: ", response);
    },

    error: function () {
      console.error("Error al enviar datos");
    },
  });
}
