<template>
  <div id="app">
    <HelloWorld/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app',
  components: {
    HelloWorld
  }
}
</script>

<style>
  #app {
    font-family: 'Montserrat', sans-serif, Arial;
    font-weight: 400;
    letter-spacing: -1px;
    font-size: 24px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    background: white;
    margin: 45px;
    padding: 10px;
  }
</style>
