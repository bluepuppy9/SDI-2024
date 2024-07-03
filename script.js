async function sendMessage() {
    if (document.getElementById('userMessage').value !== '') {
        if (document.getElementById('free')) {
            document.getElementById('free').setAttribute('id', 'typing');
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
            output.innerHTML += '<p id="responseText">' + '</p><hr>';
            output.appendChild(loadingicon);
            loadingicon.classList.remove('real');
            const responseText = document.getElementById('responseText');

            // Function to output each word with a delay
            function outputWordByWord(text) {
                // Split text into an array of words
                let words = text.split(' ');

                // Initialize index for looping through words
                let index = 0;

                // Function to output next word with delay
                function nextWord() {
                    if (index < words.length) {
                        responseText.textContent += words[index] + ' '; // Append next word
                        index++;
                        setTimeout(nextWord, 25); // Adjust delay time as needed (300ms here)
                    }
                }

                // Start outputting words
                nextWord();
            }

            // Start outputting response word by word
            outputWordByWord(data.response);
            responseText.setAttribute('id', 'gone');
            //after typing is done set the title id to free
            document.getElementById('typing').setAttribute('id', 'free');
        }
    }
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