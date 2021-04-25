function signupFormValidate() {
        if (document.signupForm.first_name.value == ""){
            document.getElementById("id_first_name_span").innerHTML="First Name should not be empty";
            document.signupForm.first_name.focus();
            return false;
            }
        else{
            document.getElementById("id_first_name_span").innerHTML="";
            }
        if (document.signupForm.email.value != ""){
            var emailID = document.signupForm.email.value;
                 atpos = emailID.indexOf("@");
                 dotpos = emailID.lastIndexOf(".");

              if (atpos < 1 || ( dotpos - atpos < 2 )) {
                  document.getElementById("id_email_span").innerHTML="Enter valid Email address";
                  document.signupForm.email.focus() ;
                  return false;
                  }
              else{
              document.getElementById("id_email_span").innerHTML="";
              }
              }
        else{
        document.getElementById("id_email_span").innerHTML="Enter valid Email address";
        document.signupForm.email.focus() ;
        return false;
        }
        if (document.signupForm.password.value != ""){
        if (document.signupForm.password.value.length < 6){
        document.getElementById("id_password_span").innerHTML="Password length should more than 6 letters";
        document.signupForm.password.focus();
        return false;
        }
        else{
        document.getElementById("id_password_span").innerHTML="";
        }
        }
        else{
        document.getElementById("id_password_span").innerHTML="Password is required";
                document.signupForm.password.focus();
                return false;
        }
        if (document.signupForm.re_password.value != ""){
                if (document.signupForm.password.value != document.signupForm.re_password.value){
                document.getElementById("id_re_password_span").innerHTML="Password is not matching";
                document.signupForm.re_password.focus();
                return false;
                }
                if (document.signupForm.password.value == document.signupForm.re_password.value){
                document.getElementById("id_re_password_span").innerHTML="";
                }
                }
        else{
                document.getElementById("id_re_password_span").innerHTML="Re-password is required";
                        document.signupForm.re_password.focus();
                        return false;
                }
        if (document.signupForm.phone_number.value != ""){
        if ((document.signupForm.phone_number.value.length == 10) || (document.signupForm.phone_number.value.length == 11)){
        document.getElementById("id_phone_number_span").innerHTML="";
        }
        else{
        document.getElementById("id_phone_number_span").innerHTML="Enate valid mobile number";
                                document.signupForm.phone_number.focus();
                                return false;
        }
        }
    return true;
    }