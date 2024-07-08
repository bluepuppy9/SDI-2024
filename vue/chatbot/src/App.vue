<template>
  <sideMenu/>
  <router-view/>
  <!--
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
  -->
</template>

<script>
import sideMenu from './components/sideMenu.vue'
export default {
  name: 'App',
  components: {
    sideMenu
  },
  setup() {

    return {}
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  word-break: break-word;
  padding: 0;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #333;
  text-decoration: none;
}

nav a.router-link-exact-active {
  background-color: #333;
  padding: 10px;
  border-radius: 4px;
  color: #ffffff;
}
</style>
