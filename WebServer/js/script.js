function RequestDataFromSocket() {
    //const inputElement = document.getElementById("InputData");
    //const data = inputElement.value;
    var DataToSend = GetSelectedElements();
    window.socket.send(DataToSend);
  };
  
  
function GetSelectedElements(){
    var photovoltaikElementsSend = [];
    var elements = document.querySelectorAll('input[name=dataSelected]:checked');

    for (let index = 0; index < elements.length; index++) {
        photovoltaikElementsSend.push("GET")
        photovoltaikElementsSend.push(elements[index].value);
    }
    return photovoltaikElementsSend.join()
}



//Timer
window.setInterval(RequestDataFromSocket, 3000)