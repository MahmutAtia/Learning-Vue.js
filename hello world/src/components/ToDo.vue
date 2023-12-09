<script>
export default {
  name: 'ToDo',
  data() {
    return {
      goals: [],
      enteredValue: '',
      link : 'https://www.youtube.com/watch?v=Wy9q22isx3U'
    }
  },

  methods: {
    addGoal() {
      this.goals.push(this.enteredValue)
      this.enteredValue = ''
    },
    removeGoal(goal) {
      this.goals.pop(goal)
    }
  }
}
</script>

<template>
  <div class="goals">
    <h2>My Goals</h2>
    <div class="row">
    <input type="text" v-model="enteredValue" />
    <button @click="addGoal">Add Goal</button>

    </div>
    <ul>
      <div v-for="goal in goals" class="row">
        <li>{{ goal }}</li>
        <button v-on:click="removeGoal(goal)">Remove Goal</button>
      </div>
    </ul>

    <a v-bind:href="link"> watch vedio</a>
  </div>
</template>

<style scoped>
h2 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.goals h2,
.goals h3 {
  text-align: center;
}

.row {
  display: flex;
  flex-wrap: wrap;
  margin: 0 -1rem;
  justify-content: space-between;
}

@media (min-width: 1024px) {
  .goals h2,
  .goals h3 {
    text-align: left;
  }
}
</style>
