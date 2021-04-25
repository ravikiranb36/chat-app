function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$(document).ready(function(){
    //Checking profile button
        $("#profile").click(function(){
            $("#profile-info").slideToggle(500);
        });

        $("#message-in").keyup(function(event){
        //If press enter in input it press send button
        if (event.which == 13){
        $("#send-btn").trigger("click");
        }
        });
});
$(document).on('submit', '#message-in-form', function(e){
    message = $("#message-in").val();
    $("#message-in").val("");
    chatSocket.send(message)
    e.preventDefault();
    if (message.length !=0){
    $.ajax({
        type:'POST',
        url:'/save-message',
        data:{
        historyId: $(".chatter-info").attr("historyId"),
        message : message,
        csrfmiddlewaretoken: csrftoken,
        },
        success:function(data){

            }
        });
    }

});

$(document).ready(function(){
    //Scrolling chat-box to down
    document.getElementById("chat_body").scrollTo(0, document.getElementById("chat_body").scrollHeight);
    //Message send button
    $("#send-btn").click(function(){
    var dt = new Date();
    var time = dt.getHours()%12 + ":" + dt.getMinutes() + '' +dt.getHours()%12 ? 'PM' : 'AM' ;
    var hours = dt.getHours()%12;
    hours = hours ? hours : 12;
    var minutes = dt.getMinutes();
    var ampm = dt.getHours()%12 ? 'PM' : 'AM';
        message=$("#message-in").val();
        if (message.length != 0){
        var mystring = `<div class="chat-sent row">
                <div class="message-container message-sent sent">
                    <img class="chat-img left" id="sender-pic" src="` + $(".chatter-info").attr("userPic")+`">
                    <span class="left sent-message">
                        <br>`+ message +
                            `<sub style= "padding-left:5px;">` + hours + ':' + minutes + ampm + `</sub>
                    </span>
                </div>
            </div>`;

        $("#chat-messages").append(mystring);
        document.getElementById("chat_body").scrollTo(0, document.getElementById("chat_body").scrollHeight);
        }

    });

});

function filterHistory() {
    var input, filter, history, list, td, i, txtValue;

  input = document.getElementById("contactSearchInput");
  filter = input.value.toUpperCase();
  history= document.getElementById("historys");
  list = history.getElementsByTagName("li");
  for (i = 0; i < list.length; i++) {
    names = list[i].getElementsByTagName("Contact")[0];
    if (names) {
      txtValue = names.innerHTML;
      if (txtValue.toUpperCase().indexOf(filter) == 0 ) {
        list[i].style.display = "";
      } else {
        list[i].style.display = "none";
      }
    }
  }
};

function checkPhoneNumber(){
    if ($("#phoneNumberInput").val().length != 10){
        alert("Mobile number should be 10 digits  Eg:9876543210");
    }
    else{
    $.ajax({
        type:"POST",
        url:"/checkContact",
        data:{
            phone_number : $("#phoneNumberInput").val(),
            csrfmiddlewaretoken: csrftoken,
        },
        success: function(data){
        var result = $.parseJSON(data);
        console.log(result["result"])
        if (result["result"] == "This phone number added to your contacts"){
            $("#searchResult").html(result["result"]);
            $("#searchResult").css("color","green");
            }else{
                $("#searchResult").html(result["result"]);
                $("#searchResult").css("color", "red");
            }
        }
        });
    }

}



