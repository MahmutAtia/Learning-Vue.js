<script>
import BaseCard from './UI/BaseCard.vue'
export default {
  name: 'AllResources',
  components: { BaseCard },
  emits: ['delete-resource'],
  props: {
    resources: Array
  },
  
}
</script>
<template>
  <div class="container">
    <BaseCard v-for="resource,idx in resources">
      <div class="row" slot="header">
        <h2>{{ resource.title }}</h2>
        <button @click="$emit('delete-resourse',idx)" class="delete-btn">delete</button>
      </div>

      <p>{{ resource.description }}</p>
      <a slot="footer" :href="resource.url">Go to Resource</a>
    </BaseCard>
  </div>
</template>

<style>
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
}

.delete-btn {
    font: inherit;
    color: teal;
    padding: 1rem 2rem;
    border-radius: 12px;
    border: 0px solid teal;
    cursor: pointer;
    }

.delete-btn:hover {
    background-color: teal;
    color: white;

    }
</style>
