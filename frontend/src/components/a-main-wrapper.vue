<template>
    <div class="a-main-wrapper">
        <a-object-acts-list/>
    </div>
    
</template>

<script>

    import aObjectActsList from "./a-object-acts-list";

    export default {
        name: "a-main-wrapper",
        components: {
            aObjectActsList,
        }
    }
</script>

<style scoped>
    .a-main-wrapper{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        max-width: 1200px;
        margin: 0 auto;
    }
</style>