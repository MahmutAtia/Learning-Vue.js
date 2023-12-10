<script>
export default {
  name: 'CounterApp',
  data: () => {
    return {
      counter: 0,
      payload: '',
      name:''
    }
  },
  methods: {
    add() {
      this.counter++
    },
    reduce() {
      this.counter--
    },
    add_payload(payload) {
      const num = payload ? parseInt(payload) : 0   
      console.log(num)
      this.counter += num
    },
    setName( e, name){
      this.name= e.target.value + ' ' + name
    }


  }
}
</script>

<template>
  <div class="counter">
    <h1> Your name is {{ name }}</h1>
    <h1>{{ counter }}</h1>
    <button v-on:click="add()">Add</button>
    <button v-on:click="reduce()">Reduce</button>

    <div class="row">
      <input type="text" v-model="payload" />
      <button v-on:click="add_payload(payload)">Add 5</button>
    </div>

    <input type="text" v-on:input="setName($event, 'Atia')" />
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.counter h2,
.counter h3 {
  text-align: center;
}

.row {
  display: flex;
  flex-wrap: wrap;
  margin: 0 -1rem;
  justify-content: space-between;
}

.counter {
  margin: 0 auto;
  max-width: 600px;
  padding: 0 var(--section-gap);
  flex-direction: column;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}
</style>
