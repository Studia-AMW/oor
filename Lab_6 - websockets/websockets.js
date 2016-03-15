var wsUri = "ws://echo.websocket.org/";
var output;
window.addEventListener("load", init, false);

function init()
{
	output = document.getElementById("output");
}

function onOpen(evt)
{
	write('<span style="color: blue;font-size:150%;">POŁĄCZONO</span>');
}

function conn(){
	websocket = new WebSocket(wsUri);
	websocket.onopen = function(evt) { onOpen(evt) };
	websocket.onclose = function(evt) { onClose(evt) };
	websocket.onmessage = function(evt) { onMessage(evt) };
	websocket.onerror = function(evt) { onError(evt) };
	document.getElementById("conn").disabled=true;
	document.getElementById("disconn").disabled=false;
}

function disconn(){
	websocket.close();
	document.getElementById("conn").disabled=false;
	document.getElementById("disconn").disabled=true;
	
}

function send(){
	var mess = document.getElementById('tekst').value;
	doSend(mess);
	document.getElementById("tekst").value="";
}
function onClose(evt)
{
	write('<span style="color: red;font-size:150%;"<h2>ROZŁĄCZONO</h2></span>');
}

function onMessage(evt)
{
	write('<span style="color: blue;">Odpowiedź: ' + evt.data+'</span>');
}

function onError(evt)
{
	write('<span style="color: red;">BŁĄD:</span> ' + evt.data);
}

function doSend(message)
{
	write("Wysłano: " + message);
	websocket.send(message);
}

function write(message)
{
	var pre = document.createElement("p");
	pre.style.wordWrap = "break-word";
	pre.innerHTML = message;
	output.appendChild(pre);
}
