async function sendMessage() {
    if (document.getElementById('userMessage').value !== '') {
        if (document.getElementById('free')) {
            const output = document.getElementById('returnarea');
            const userBubble = document.getElementById('userbubble');
            const userMessage = document.getElementById('userMessage').value;
            output.innerHTML += '<p id="messageplaceholder"class="response" style="visibility: hidden;">' + userMessage + '</p>';
            userBubble.innerHTML += '<p class="response"">' + userMessage + '</p>';
            document.getElementById('free').setAttribute('id', 'typing');
            var loadingicon = document.getElementById('loadingIcon');
            loadingicon.classList.add('real');
            triggerAnimation();
            loadingAnimation();
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
            //will output the message into the response area but invsibile so it takes up space
            output.innerHTML += '<p id="responseText" class="response">' + '</p>';
        
            userBubble.innerHTML += '<p id="messageplaceholder"class="response" style="visibility: hidden;">' + data.response + '</p>';
            output.appendChild(loadingicon);
            loadingicon.classList.remove('real');
            const responseText = document.getElementById('responseText');
            //const messageplaceholder = document.getElementById('messageplaceholder');

            // Function to output each word with a delay
            function outputWordByWord(text, placeholder) {
                // Split text into an array of words
                let words = text.split(' ');
                let wordsplace = placeholder.split(' ');
                // Initialize index for looping through words
                let index = 0;
                indexp = 0;
                //wordsplacefullsplit = [];
                //for (let i = 0; i < wordsplace.length; i++) {
                //    wordsplacefullsplit.push(wordsplace[i].split(''));
                //}
                //console.log(wordsplacefullsplit);
                // Function to output next word with delay
                //function nextWordplace() {
                //    if (index < words.length) {
                //        responseText.textContent += words[index] + ' '; // Append next word
                //        index++;
                //        setTimeout(nextWord, 25);
                //        document.getElementById('chatbox').scrollTop = document.getElementById('chatbox').scrollHeight; // Adjust delay time as needed (300ms here)
                //    }
                //}
//
                //// Start outputting words
                //nextWordplace();

                function nextWord() {
                    if (index < words.length) {
                        responseText.textContent += words[index] + ' '; // Append next word
                        index++;
                        setTimeout(nextWord, 25);
                        document.getElementById('chatbox').scrollTop = document.getElementById('chatbox').scrollHeight; // Adjust delay time as needed (300ms here)
                    } else {
                        document.getElementById('typing').setAttribute('id', 'free');
                    }
                }

                // Start outputting words
                nextWord();
            }

            // Start outputting response word by word
            outputWordByWord(data.response, userMessage);
            responseText.setAttribute('id', 'gone');
            //messageplaceholder.setAttribute('id', 'gone');
            //after typing is done set the title id to free
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