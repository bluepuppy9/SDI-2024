<template>
    <div>
        <form @submit.prevent="animateSend">
            <input type="text" id="message" v-model="message">
            <button type="submit" id="submit" @click="!messageSent && message.trim() ? $emit('submitted', [message, chatNumber++]) : null;">
                <img src="https://static.thenounproject.com/png/3553333-200.png" id="sendicon" alt="submit" :class="classname">
            </button>
        </form>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    data() {
        return {
            message: '',
            messageSent: false,
            classname: 'none',
            chatNumber: 0
        }
    },
    methods: {
        animateSend() {
            if(!this.messageSent) {
                this.message = '';
                this.messageSent = true;
                this.classname = 'animate';
                //remove the messagesent false from timeout once ai is put in
                setTimeout(() => {
                    this.classname = 'none';
                    this.messageSent = false; //change this later to only after response is made
                }, 300);
            }
    }
}
}
</script>

<style>
    #submit {
        border-radius: 10px;
        background-color: #696969;
        border: none;
        cursor: pointer;
        padding: 10px;
    }

    #submit:hover {
        background-color: #808080;
    }

    #sendicon {
        width: 40px;
        height: 40px;
    }

    @keyframes animation {
        0% {
            transform: scale(1);
        }

        50% {
            transform: scale(1.2);
        }

        100% {
            transform: scale(1);
        }
    }

    .animate {
        animation: animation 0.3s ease-in-out;
    }
    
    form {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
        background-color: #696969;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        margin: 10px auto;
    }
    #message {
        width:90%;
        border-radius: 30px;
        padding: 15px;
        font-size: 20px;
        justify-self: center;
    }
</style>