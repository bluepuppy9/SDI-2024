<template>
    <div id="chat">
        <div v-for="message, index in userMessages" :key="message" class="userChats">
            <p class ="msg">{{message}}</p>
            <div class ="botChats">
                <p class ="msg">{{BotMessages[index]}}</p>
            </div>
        </div>
    </div>

    <InputBar id="inputBar" @submitted="updateData" @chatUpdated="console.log('chatUpdated')"/>
    
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
        // Function to output each word with a delay
        async function outputWordByWord(text) {
            let words = text.split(' ');
        
            function delay() {
                return new Promise(resolve => setTimeout(resolve, 25));
            }
        
            for (let i = 0; i < words.length; i++) {
                // Update only the current bot message
                BotMessages.value[currentResponseNumber.value] += words[i] + ' ';
                await delay();
            }
        }
        const currentBotMessage = computed(() => {
            return BotMessages.value[currentResponseNumber.value];
        })
        async function updateData(message) {
            //console.log(message[0]);
            message[0].toLowerCase();
            userMessages.value.push(message[0]);
            currentResponseNumber.value = message[1];
            BotMessages.value.push('');
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
            fetch('http://localhost:5000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message[0]
                })
                })
                .then(response => response.json())
                .then(data => outputWordByWord(data.response))
                .catch(error => console.error(error))
        }
        return {
        userMessages, updateData, BotMessages, currentResponseNumber, currentBotMessage
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
    }

    .botChats {
        display: flex;
        flex-direction: column;
        width: 100%;
    }
</style>