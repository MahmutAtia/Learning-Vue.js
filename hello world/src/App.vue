<script >
import ToDo from './components/ToDo.vue';
import CounterApp from './components/CounterApp.vue';


export default {
    name: 'App',
    data() {
        return {
            name: 'Hello World!'
        };
    },
    components: { ToDo, CounterApp }
}

</script>

<template>
  <div class="container"></div>
  <CounterApp />
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  .container {
    display: flex;
    /* flex-wrap: wrap; */
    justify-content: center;
    align-items: center;
  }
}
</style>
