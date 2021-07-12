<template>
    <tr>
        <td>{{object_data.create_date}}</td>
        <td>{{object_data.address}}</td>
        <td>{{object_data.work}}</td>
        <td>
            <button>copy</button>
        </td>
        <td>
            <button>edit</button>
        </td>
        <td>
            <button>file</button>
        </td>
        <td>
            <button>delete</button>
        </td>
    </tr>
</template>

<script>
    export default {
        name: "a-object-act-item",
        props: {
            object_data: {
                type: Object,
                default() {
                    return {}
                }
            }
        }
    }
</script>

<style scoped>

</style>