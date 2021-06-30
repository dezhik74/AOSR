<template>
  <div id="app">
    <h1> Привет vue</h1>
    <a-main-wrapper/>
  </div>
</template>

<script>

  import aMainWrapper from "./components/a-main-wrapper";

  export default {
    name: 'App',
    components: {
      aMainWrapper,
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 20px;}
</style>
