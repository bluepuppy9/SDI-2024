async function sendMessage() {
    triggerAnimation();
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
    if(data.response == "") {
        document.getElementById('response').innerHTML += '<p>' + data.response + '</p>';
    } else {
        document.getElementById('response').innerHTML += '<p>' + data.response + '</p>' + '<hr>';
    }
}

function triggerAnimation() {
    const button = document.getElementById('sendButton');
    button.classList.add('animate');
    button.addEventListener('animationend', () => {
        button.classList.remove('animate');
    }, { once: true });
}