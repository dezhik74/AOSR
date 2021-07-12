<template>
    <div class="a-object-acts-list">
        <table>
            <tr>
                <th>Дата</th>
                <th>Адрес</th>
                <th>Вид работ</th>
            </tr>
            <a-object-acts-item
                v-for="object in objectsdata"
                :key="object.id"
                v-bind:object_data="object"
            />

        </table>
    </div>
</template>

<script>

    import aObjectActsItem from './a-object-act-item'
    export default {
        name: "a-object-acts-list",
        components: {
            aObjectActsItem
        },
        props: {},
        data() {
            return {
                objectsdata: [
                    {
                        id: 1,
                        create_date: '2021-06-27',
                        address: 'Большой пр. В.О., д.82 литера А',
                        work: 'Капитальный ремонт системы холодного водоснабжения'
                    },
                    {
                        id: 2,
                        create_date: '2021-06-27',
                        address: '4-я линия В.О., д.5 литера А',
                        work: 'Капитальный ремонт системы водоотведения'
                    }
                ]

            }
        },
        computed: {},
        methods: {},
        watch: {},
        mounted() {
        }
    }
</script>

<style scoped>
    .a-object-acts-list {
        width: 100%;
        max-width: 100%;
    }

    table {
        width: 100%;
    }

</style>