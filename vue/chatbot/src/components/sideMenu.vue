<template>
    <!--create background for the entire screen thats partly transparent-->
    <div v-show="menuClicked" id="background"></div>
    <div v-show="menuClicked" id="menu" ref="menu">
        <div id="login" @click="login">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" id="loginIcon">
            <p id="loginText">Login</p>
        </div>
    </div>
    <img @click="handleClick" src="https://cdn-icons-png.flaticon.com/128/5358/5358672.png" id="menuIcon" alt="menu">
    <loginForm v-if="loginActive" @close="loginActive = !loginActive"/>
</template>
<script>
import { ref } from 'vue';
import loginForm from './loginForm.vue'
export default {
    name: 'sideMenu',
    components: {
        loginForm
    },
    setup() {
        const menuClicked = ref(false);
        const menu = ref(null);
        const loginActive = ref(false);
        function login () {
            loginActive.value = !loginActive.value
            menu.value.classList.remove('open')
            menuClicked.value = !menuClicked.value
        }
        function handleClick() {
            menu.value.classList.remove('open')
            menuClicked.value = !menuClicked.value
            if(menu.value.classList.contains('open')) {
                menu.value.classList.remove('open')
            }
            menu.value.classList.add('open')
        }
        return { menuClicked, menu, handleClick, loginActive, login };
    },
}
</script>

<style>

    @keyframes openAnimation {
            0% {
                transform: translateX(-100%);
            }

            100% {
                transform: translateX(0px);
            }
        }
    #menuIcon {
        width: 40px;
        height: 40px;
        position: fixed;
        top: 10px;
        left: 10px;
        visibility: visible;
        cursor: pointer;
    }

    #menu {
        position: fixed;
        display: flex;
        top: 0;
        left: 0;
        width: 200px;
        height: 100vh;
        background-color: hsl(0, 0%, 79%);
        padding-left: 10px;
        padding-right: 10px;
        flex-direction: column;
        overflow-y: scroll;
        scrollbar-width:thin;
    }

    .open {
        animation: openAnimation 0.3s ease-in-out;
    }

    #background {
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        position: fixed;
        background-color: rgba(0, 0, 0, 0.5);
    }
    #loginIcon {
        width: 60px;
        height: 60px;
    }
    #login {
        display: flex;
        margin-top: 60px;
        cursor: pointer;
    }

    #loginText {
        margin-left: 10px;
        font-size: 20px;
        font-weight: bold;
    }
</style>