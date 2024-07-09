<template>
    <div id="chat" ref="chat">
        <div v-for="message, index in userMessages" :key="message" class="userChats">
            <p class ="msg">{{message}}</p>
            <div class ="botChats">
                <p class ="msg">{{BotMessages[index]}}</p>
            </div>
        </div>
    </div>

    <InputBar id="inputBar" :MessageInProgess="MessageInProgess" @submitted="updateData" @chatUpdated="console.log('chatUpdated')"/>
    
</template>

<script>
import { computed, ref } from 'vue';
import InputBar from './InputBar.vue';
export default {
    name: 'chatBox',
    components: {
        InputBar
    },
    setup() {
        const currentResponseNumber = ref(null);
        const userMessages = ref([
            
        ]);
        const BotMessages = ref([
            
        ]);
        const MessageInProgess = ref(false);
        const chat = ref(null);
        const chatlogUser = ref(null);
        const chatlogBot = ref('Nothing yet');
        // Function to output each word with a delay
        async function outputWordByWord(text) {
            let words = text.split(' ');
            chatlogBot.value = text;
            function delay() {
                return new Promise(resolve => setTimeout(resolve, 25));
            }
            BotMessages.value.push('');
        
            for (let i = 0; i < words.length; i++) {
                // Update only the current bot message
                BotMessages.value[currentResponseNumber.value] += words[i] + ' ';
                chat.value.scrollTop = chat.value.scrollHeight;
                await delay();
            }
        }
        async function updateData(message) {
            //console.log(message[0]);
            MessageInProgess.value = true;
            message[0].toLowerCase();
            userMessages.value.push(message[0]);
            chat.value.scrollTop = chat.value.scrollHeight;
            currentResponseNumber.value = message[1];
            //check length of user message and bot message and trim if its longer than 10
            //if (userMessages.value.length > 10) {
            //    userMessages.value.shift();
            //}
            //if(message[0] == 'hi') {
            //    outputWordByWord('Hi, I am an AI. Ask me anything!');
            //} else if(message[0] == 'bye') {
            //    outputWordByWord('Bye!');
            //} else {
            //    outputWordByWord(message[0]);
            //}
            //console.log(ChatMessages.value);
            //console.log(message)
            // Update the message in the data property
            //send message to chatbox
             const data = await fetch('http://localhost:5000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    //send only up to the last 10 user messages
                    //message: 'current message: ' +message[0] + ' | BotMessageLog(you): ' + chatlogBot.value + ' | UserMessageLog: ' + chatlogUser.value + ' | do not give me the logs and keep replies short'
                    message: 'respond to this message(response is sent to user)response should be 3 sentence max unless asked otherwise: ' +message[0] + ' | UserMessageLog: ' + chatlogUser.value
                })
                })
                .then(response => response.json())
                .then(data => outputWordByWord(data.response))
                .catch(error => console.error(error))

            MessageInProgess.value = false;
            chatlogUser.value = userMessages.value
            }
        return {
        userMessages, updateData, BotMessages, currentResponseNumber, MessageInProgess,
        chat
        }
    }
}
</script>

<style>
    #chat {
        border: 1px solid black;
        padding: 10px;
        height: calc(100vh - 210px);
        display: flex;
        flex-direction: column;
        align-items: center;
        border-radius: 10px;
        overflow: hidden;
        overflow-y: scroll;
        /*move scroll bar to left*/
        scrollbar-width: none;
        word-break: break-word;        
    }

    .userChats {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
        align-items: flex-end;
        align-self: flex-end;
        width: 100%;
    }

    .msg {
        background-color: lightgray;
        border-radius: 10px;
        padding: 10px;
        margin: 5px;
        width: fit-content;
        max-width: 80%;
        text-align: left;
    }

    .botChats {
        display: flex;
        flex-direction: column;
        width: 100%;
    }
</style>