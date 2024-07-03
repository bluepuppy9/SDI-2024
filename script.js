async function sendMessage() {
    var loadingicon = document.getElementById('loadingIcon');
    loadingicon.classList.add('real');
    triggerAnimation();
    loadingAnimation();
    const userMessage = document.getElementById('userMessage').value;
    document.getElementById('userMessage').value = '';
    const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
    });
    const data = await response.json();
    console.log(data);
    loadingicon.remove();
    const output = document.getElementById('response');
    if (data.response == "") {
        output.innerHTML += '<p>' + data.response + '</p>';
    } else {
        output.innerHTML += '<p>' + data.response + '</p>' + '<hr>';
    }
    output.appendChild(loadingicon);
    loadingicon.classList.remove('real');
}

function triggerAnimation() {
    const button = document.getElementById('sendButton');
    button.classList.add('animate');
    button.addEventListener('animationend', () => {
        button.classList.remove('animate');
    }, { once: true });
}

function loadingAnimation() {
    var loadingicon = document.getElementById('loadingIcon');
    loadingicon.classList.add('animate');
    document.getElementById('chatbox').scrollTop = document.getElementById('chatbox').scrollHeight;
}