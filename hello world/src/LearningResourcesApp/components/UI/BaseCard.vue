<script>
export default {
    name: 'BaseCard' }
    
</script>
<template>

    <div class="base-card">
        <header>
            <slot name="header"></slot>
        </header>
        <div class="content">
            <slot></slot>
        </div>
        <footer>
            <slot name="footer"></slot>
        </footer>


    </div>
 
  
</template>

<style>
.base-card {
    border-radius: 12px;
    background-color: #fff;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    padding: 1rem;
    margin: 1rem auto;
    width: 90%;
    max-width: 40rem;
}


</style>