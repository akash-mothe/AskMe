    
function showHidePass(){
    var login_input = document.getElementById("id_password");
    var show_btn = document.getElementById("show_pass");
    var hide_btn = document.getElementById("hide_pass");
    if (login_input.type === "password") {
      login_input.type = "text";
      show_btn.style.display = 'none';
      hide_btn.style.display = 'block';
    } else {
      login_input.type = "password";
      show_btn.style.display = 'block';
      hide_btn.style.display = 'none';
    }
  }