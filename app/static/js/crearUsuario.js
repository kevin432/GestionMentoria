$(document).ready(function () {
  iniciarFormulario();
});

function iniciarFormulario() {
  $("#crear_user").on("submit", function (e) {
    e.preventDefault();

    let datos = obtenerDatos();

    if (validarDatos(datos)) {
      enviarDatos(datos);
    }
  });
}

function obtenerDatos() {
  return {
    nombre: $("#nombre").val().trim(),
    email: $("#email").val().trim(),
    password: $("#password").val().trim(),
  };
}

function validarDatos(data) {
  if (data.nombre === "" || data.email === "" || data.password === "") {
    alert("Todos los campos son obligatorios");
    return false;
  }
  return true;
}

function enviarDatos(datos) {
  $.ajax({
    url: "/crear",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(datos),

    success: function (response) {
      console.log("✅ RESPUESTA DEL SERVIDOR:", response);
    },

    error: function () {
      console.error("❌ Error al enviar datos");
    },
  });
}
