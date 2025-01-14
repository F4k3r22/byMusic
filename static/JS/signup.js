$(document).ready(function() {
  // Configuración general del validador
  $.validator.setDefaults({
      errorElement: 'span',
      errorClass: 'validate-tooltip'
  });

  // Validación del formulario
  $("form").validate({
      rules: {
          name: {
              required: true,
              minlength: 2
          },
          email: {
              required: true,
              email: true
          },
          pno: {
              required: true,
              minlength: 4,
              maxlength: 15,
              digits: true
          },
          password: {
              required: true,
              minlength: 6
          },
          cnfPassword: {
              required: true,
              equalTo: "[name='password']"
          },
          gender: {
              required: true
          },
          countryCode: {
              required: true
          }
      },
      messages: {
          name: {
              required: "Por favor ingresa tu nombre",
              minlength: "El nombre debe tener al menos 2 caracteres"
          },
          email: {
              required: "Por favor ingresa tu email",
              email: "Por favor ingresa un email válido"
          },
          pno: {
              required: "Por favor ingresa tu número de teléfono",
              minlength: "El número debe tener al menos 9 dígitos",
              maxlength: "El número no debe exceder 15 dígitos",
              digits: "Por favor ingresa solo números"
          },
          password: {
              required: "Por favor ingresa una contraseña",
              minlength: "La contraseña debe tener al menos 6 caracteres"
          },
          cnfPassword: {
              required: "Por favor confirma tu contraseña",
              equalTo: "Las contraseñas no coinciden"
          },
          gender: {
              required: "Por favor selecciona tu género"
          },
          countryCode: {
              required: "Por favor selecciona el código de país"
          }
      },
      submitHandler: function(form) {
          // Combinar el código de país y el número de teléfono
          const countryCode = $('[name="countryCode"]').val();
          const phoneNumber = $('[name="pno"]').val();
          
          // Asegurarse de que ambos valores existen antes de combinarlos
          if (countryCode && phoneNumber) {
              const fullPhoneNumber = countryCode + phoneNumber;
              
              // Actualizar el valor del campo pno con el número completo
              $('[name="pno"]').val(fullPhoneNumber);
          }
          
          // Enviar el formulario
          form.submit();
      },
      // Mostrar errores en un formato más amigable
      errorPlacement: function(error, element) {
          error.addClass('text-red-500 text-sm mt-1');
          error.insertAfter(element);
      },
      // Resaltar campos con error
      highlight: function(element) {
          $(element).addClass('border-red-500');
      },
      // Quitar resaltado cuando se corrige el error
      unhighlight: function(element) {
          $(element).removeClass('border-red-500');
      }
  });
});