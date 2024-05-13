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


// Filter for complete and cancelled status in the run queue
document.addEventListener('DOMContentLoaded', function() {
    var statusRows = document.querySelectorAll('.status-row');
    statusRows.forEach(function(row) {
        if (row.querySelector('.status').innerText.toLowerCase() === 'complete' ||
            row.querySelector('.status').innerText.toLowerCase() === 'cancelled') {
            row.classList.add('hidden');
        }
    });
});


