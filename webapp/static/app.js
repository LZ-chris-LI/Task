// Prompt user for their username
var username = prompt("Enter your username:");
document.querySelector("#username").textContent = username;

// Establish WebSocket connection
var socket = new WebSocket(`ws://${window.location.host}/ws/${username}`);

// Handle WebSocket connection errors
socket.onerror = function(error) {
    console.error("Connection Error: ", error);
    alert("Connection error!");
};

// Handle incoming messages
socket.onmessage = function(event) {
    var messages = document.getElementById('messages');
    var message = document.createElement('li');
    var content = document.createTextNode(event.data);
    message.appendChild(content);
    messages.appendChild(message);
};

// Handle WebSocket connection close
socket.onclose = function(event) {
    console.log("Connection closed: ", event);
    alert("Connection closed! Please refresh to restart!");
};

// Send message through WebSocket
function sendMessage(event) {
    var input = document.getElementById("inputMessage");
    var message = input.value.trim();
    if (message !== ""){        // verify empty input
        socket.send(input.value);
        input.value = '';
    } else {
        alert("Please enter a message.");
    }
    event.preventDefault();
}
