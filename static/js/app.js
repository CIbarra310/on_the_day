// Message Timer
var messageTimeout = document.getElementById("message-timer");

function hideMessage() {
    if (messageTimeout) {
        // Only access the style property if messageTimeout is not null
        messageTimeout.style.display = "none";
    }
}

// Call hideMessage after 2 seconds (2000 milliseconds)
setTimeout(hideMessage, 2000);