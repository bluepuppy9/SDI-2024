<template>
  <div class="home">
    <h1>Home</h1>
    <chatBox/>
  </div>
</template>

<script>
import chatBox from '@/components/chatBox.vue'
import { ref } from 'vue';

export default {
  name: 'HomeView',
  components: {
    chatBox
  },
}
</script>
<style>
</style>
