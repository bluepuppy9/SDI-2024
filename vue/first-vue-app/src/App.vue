<template>
  <div id="app">
    <HelloWorld></HelloWorld>
    <nav class="navbar" :class="{ responsive: isResponsive }">
      <a href="#" class="navbar-item">Home</a>
      <a href="#" class="navbar-item">About</a>
      <a href="#" class="navbar-item">Contact</a>
      <a href="javascript:void(0);" class="icon" @click="toggleNavbar">&#9776;</a>
    </nav>

    <div class="content">
      <h1>Welcome to My Website</h1>
      <p>Resize the browser window to see the responsive effect.</p>
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
export default {
  name: 'App',
  data() {
    return {
      isResponsive: false,
    };
  },
  methods: {
    toggleNavbar() {
      this.isResponsive = !this.isResponsive;
    },
  },
  components: {
    HelloWorld,
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

.navbar {
  background-color: #333;
  overflow: hidden;
}

.navbar-item {
  float: left;
  display: block;
  color: white;
  text-align: center;
  padding: 14px 20px;
  text-decoration: none;
}

.navbar-item:hover {
  background-color: #ddd;
  color: black;
}

.icon {
  display: none;
}

.content {
  padding: 16px;
}

@media screen and (max-width: 600px) {
  .navbar-item:not(:first-child) {
    display: none;
  }
  .icon {
    float: right;
    display: block;
  }
}

@media screen and (max-width: 600px) {
  .navbar.responsive {
    position: relative;
  }
  .navbar.responsive .icon {
    position: absolute;
    right: 0;
    top: 0;
  }
  .navbar.responsive .navbar-item {
    float: none;
    display: block;
    text-align: left;
  }
}
</style>