<template>
    <div @click.self="this.$emit('close')" id="backgroundLogin" style="width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); position: fixed; top: 0; left: 0;">
        <form id="loginForm">
            <label>Email</label>
            <input type="email" id="email">
            <label>Password</label>
            <input type="password" id="password">
        </form>
    </div>
</template>

<script>
export default {
    name: 'loginForm',
}
</script>

<style>
    #loginForm {
        display: flex;
        flex-direction: column;
        border: 1px solid black;
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        align-items: flex-start;
        max-width: 80%;
    }

    #loginForm input {
        margin-bottom: 10px;
        padding: 5px;
        border-radius: 10px;
        border: 1px solid black;
    }
    
    #loginForm label {
        font-weight: bold;
        margin-bottom: 5px;
    }

    #backgroundLogin {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>