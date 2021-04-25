//function createSocket(){
//    const roomName = $(".history_link").attr("id");
//            console.log("creating socket");
//            const chatSocket = new WebSocket(
//                'ws://'
//                + window.location.host
//                + '/ws/chat/'
//                + roomName
//                + '/'
//            );
//            chatSocket.onopen = () => {
//                             console.log("WebSocket open");
//                           };
//            chatSocket.onmessage = function(e) {
//                        console.log("onmessage")
//                    };
//
//                    chatSocket.onclose = function(e) {
//                        console.error('Chat socket closed unexpectedly');
//                    };
//}

function createHistory(phoneNumber){
    $.ajax({
            type:"POST",
            url:"/createHistory",
            data:{
                phone_number : phoneNumber,
                csrfmiddlewaretoken: csrftoken,
            },
            success: function(data){
            console.log("History created");
            location.reload(true);
            }

        });
}

