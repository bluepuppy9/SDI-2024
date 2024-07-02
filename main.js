async function sendMessage() {
    triggerAnimation();
    const userMessage = document.getElementById('userMessage').value;
    const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
    });
    const data = await response.json();
    console.log(data);
    document.getElementById('response').innerHTML += '<p>' + data.response + '</p>' + '<hr>';
    document.getElementById('userMessage').value = '';
}

function triggerAnimation() {
    const button = document.getElementById('sendButton');
    button.classList.add('animate');
    button.addEventListener('animationend', () => {
        button.classList.remove('animate');
    }, { once: true });
}