
+ function($) {
    $('.palceholder').click(function() {
      $(this).siblings('input').focus();
    });
  
    $('.form-control').focus(function() {
      $(this).parent().addClass("focused");
    });
  
    $('.form-control').blur(function() {
      var $this = $(this);
      if ($this.val().length == 0)
        $(this).parent().removeClass("focused");
    });
    $('.form-control').blur();
  
    // Validetion
    $.validator.setDefaults({
      errorElement: 'span',
      errorClass: 'validate-tooltip'
    });
    $("#formvalidate").validate({
      rules: {
        userName: {
          required: true,
          minlength: 6
        },
        userPassword: {
          required: true,
          minlength: 6
        },
        // La regla 'terms' debe estar dentro del objeto 'rules'
        terms: {
          required: true
        } 
      },
      messages: {
        userName: {
          required: "Please enter your username.",
          minlength: "Please provide valid username."
        },
        userPassword: {
          required: "Enter your password to Login.",
          minlength: "Incorrect login or password."
        },
        // Agregar el mensaje de error para el checkbox
        terms: {
          required: "Debes aceptar los términos y condiciones"
        }
      }
    });
  }(jQuery);
