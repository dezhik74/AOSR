<template>
  <div id="app">
    <h1> Привет vue</h1>
    <ObjectActsList/>
  </div>
</template>

<script>

  import ObjectActsList from "./components/objectactslist";

  export default {
    name: 'App',
    components: {
      ObjectActsList,
    }
}
</script>

<style>
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  max-width: 1200px;
  margin: 0 auto;
}
</style>
