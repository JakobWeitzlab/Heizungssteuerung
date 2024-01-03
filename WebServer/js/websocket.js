let socket = new WebSocket("ws://localhost:8765");

if(socket.readyState === socket.CLOSED){
  let socket = new WebSocket("ws://localhost:8765");
  window.socket = socket;
}

socket.onopen = function(e) {
  window.socket = socket;
  socket.addEventListener("message", (event) => {
    const arrData = event.data.split(",");
    //alert(arrData)
    DisplayData(arrData);
  });
};

socket.onclose = function(event) {
  if (event.wasClean) {
    alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    // e.g. server process killed or network down
    // event.code is usually 1006 in this case
    alert('[close] Connection died');
    alert(event.code)
  }
};

socket.onerror = function(error) {
  alert(`[error]`);
};


function DisplayData(dataArr){
  const produktionTagArr = [];
  const produktionJetztArr = [];

  dataArr.forEach((element, index) => {
    if(element === "E_Day"){
      produktionTagArr.push(dataArr[index+1])
    }
    if(element === "P"){
      produktionJetztArr.push(dataArr[index+1])
    }

    const produktionTagDiv = document.querySelectorAll(".produktionTag");
    const produktionJetztDiv = document.querySelectorAll(".produktionJetzt");

    produktionTagDiv.forEach((element, index) => {
      element.innerHTML=`Produktion_Tag: ${produktionTagArr[index]}`;
    });
    produktionJetztDiv.forEach((element, index) => {
      element.innerHTML=`Produktion_Jetzt: ${produktionJetztArr[index]}`;
    });

  });
  
}