<script>
import AllResources from './components/AllResources.vue';
import AddResource from './components/AddResource.vue'; 

export default {
  name: 'MainApp',
  data() {
    return {
      currentComponent: 'AllResources',
      resources: [
        {
          title: 'Learn Vue',
          description: 'Learn Vue.js - it\'s easy!',
          url: 'https://vuejs.org'
        },
        {
          title: 'Learn React',
          description: 'Learn React.js - it\'s easy!',
          url: 'https://reactjs.org'
        },
        {
          title: 'Learn Angular',
          description: 'Learn Angular - it\'s easy!',
          url: 'https://angular.io'
        }
      ]
    };
  },
  components: { AllResources , AddResource},
  methods: {
    deleteResource(idx) {
      console.log('deleteResource', idx);
      this.resources.splice(idx, 1);
    },
    setCurrentComponent(componentName) {
      this.currentComponent = componentName;

    },
    AddResource(newResource) {
      this.resources.push(newResource);
      this.setCurrentComponent('AllResources');
    }
  }

}
</script>


<template>
    <header class="navigate">

      <button class="header-btn" @click="setCurrentComponent('AllResources')">All Resources</button>
      <button class="header-btn" @click="setCurrentComponent('AddResource')">Add Resource</button>

    </header>


    <KeepAlive>
    <component :is="currentComponent"   :resources="resources" @delete-resourse="deleteResource" @add-resource="AddResource">
    

    </component>
  </KeepAlive>

    



</template>

<style>

.navigate {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.header-btn {
  font: inherit;
  color: teal;
  padding: 1rem 2rem;
  border-radius: 12px;
  border: 0px solid teal;
  cursor: pointer;
  margin: 1rem;
}

</style>