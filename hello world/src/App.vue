<script >
// import ToDo from './components/ToDo.vue';
// import CounterApp from './components/CounterApp.vue';
import MonsterGame from './components/MonsterGame.vue';
import MainApp from './LearningResourcesApp/Main.vue';


export default {
    name: 'App',
    components: { MainApp },
    data() {
        return {
            name: 'Hello World!'
        };
    },
    components: { MainApp,MonsterGame }
}

</script>

<template>
  <MainApp/>
  
  
</template>
<!-- 
<style  scoped>
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
</style> -->
