<script>
export default {
    name: 'AddResource',
    data() {
        return {
            title: '',
            description: '',
            url: '',
            dialogOpen: false
        };
    },
    methods: {
        addResource() {

            if (this.title === '' || this.description === '' || this.url === '') {
               
                this.dialogOpen = true;
                return;
            }
            const newResource = {
                title: this.title,
                description: this.description,
                url: this.url
            };
            this.$emit('add-resource', newResource);
            this.title = '';
            this.description = '';
            this.url = '';
        }
    }
}


</script>

<template>
    <div class="container">

        <div class="row">
            <label for="title">Title</label>
            <input type="text" id="title" v-model="title">
        </div>
        <div class="row">
            <label for="description">Description</label>
            <input type="text" id="description" v-model="description">
        </div>
        <div class="row">
            <label for="url">URL</label>
            <input type="text" id="url" v-model="url">
        </div>
        <div class="row">
            <button @click="addResource">Add Resource</button>
        </div>

    </div>

    <Teleport to="body">
    <dialog open v-if="dialogOpen">
        <h2>Are you sure?</h2>
        <p>You have not filled out all fields.</p>
        <button @click="dialogOpen=false">Ok</button>
        
    </dialog>
    </Teleport>
</template>

<style>

.container {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    
}

.row {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    margin: 1rem;
    width: 50%;
}

label {
    font-weight: bold;
    margin-right: 1rem;
}

input {
    font: inherit;
    padding: 0.5rem;
    border-radius: 12px;
    border: 1px solid teal;
    width: 20rem;
}

button {
    font: inherit;
    color: teal;
    padding: 1rem 2rem;
    border-radius: 12px;
    border: 0px solid teal;
    cursor: pointer;
    margin: 1rem;
    margin: auto;
    }
dialog {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);


}
</style>