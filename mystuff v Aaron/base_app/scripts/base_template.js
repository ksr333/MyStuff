$(function(){
    $("#login_button").click(function(){
        $('body').loadmodal({
            id: 'login_modal',
            title: 'Login',
            url: '/customer/login/',
        });
	});

    $("#password_edit_button").click(function(){
        $('body').loadmodal({
            id: 'password_edit_modal',
            title: 'Change Password',
            url: '/customer/password_edit/',
        });
	});

    $("#logo").click(function(){
      $('img').css({
          width: '10em',
          height: '10em'
      });
    });

    $("#footer_logo").mouseover(function(){
      $("#test").each(function() {
        $(".div").css("background-color", "red");
      });
    });

    $("#login_button").mouseover(function(){
        $("#login_button").css("background-color", "#E0E0E0" );
        $("#login_button").css("color", "black");
    });

    $("#login_button").mouseleave(function(){
       $("#login_button").css("background-color", "white");
       $("#login_button").css("color", "black");
    });

    $("#username").mouseover(function(){
        $("#username").css("background-color", "#E0E0E0" );
        $("#username").css("color", "black");

    });
    $("#username").mouseleave(function(){
       $("#username").css("background-color", "white");
       $("#username").css("color", "black");
    });

});//ready
