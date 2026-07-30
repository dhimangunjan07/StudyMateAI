function clearChat(){

document.getElementById("chatBox").innerHTML="";

}

window.onload=function(){

var chat=document.getElementById("chatBox");

if(chat){

chat.scrollTop=chat.scrollHeight;

}

}