<script setup>
import { ref, computed, onMounted } from 'vue'; 
import { useMessageStore } from '@/stores/messageStore';
import { useAuthStore } from '@/stores/auth_store';

import { useRoute, useRouter } from 'vue-router';

import product from '@/components/product.vue';
// import { c } from 'vite/dist/node/types.d-aGj9QkWt';

const authStore = useAuthStore();
const messageStore = useMessageStore();

const backend_url = computed(() => authStore.getBackendServerURL());

const props = defineProps({
  category_id : {
    type: Number,
    required: true
  }
})
console.log(props.category_id)
const category = ref(null)

const fetchCategory = function(){
    fetch(
        `${backend_url.value}/api/v1/category/${props.category_id}`,
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authentication-Token': authStore.getAuthToken(),
                'Access-Control-Allow-Origin': '*'
            }
        }
    ).then(response => response.json()).then(data=>
        {
            // console.log(data);
            category.value = data;
            // console.log(category.value)
        }
    )
}

const deleteCategory = function(category_id){
    fetch(
        `${backend_url.value}/api/v1/category/${category_id}`,
        {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authentication-Token': authStore.getAuthToken(),
                'Access-Control-Allow-Origin': '*'
            }
        }
    ).then(response => response.json()).then(data=>
        {
            // console.log(data);
            messageStore.setFlashMessage(data.message);
            fetchCategory();
        }
    )
}


onMounted(()=>{
    fetchCategory()
})

</script>


<template>
<div>
    <h1>Category</h1>
    <div v-if="category">
        <h2>{{category.category_name}}</h2>
        <p>{{category.category_description}}</p>
        {{ `${backend_url.value}/api/v1/category/${category_id}` }}
        <button @click="deleteCategory(category.category_id)">Delete</button>

        <div class="border">
            <product v-for="product in category.products" :product_id = product.product_id />
        </div>
        <!-- do it edit also -->
    </div>
    <div v-else>
        <p>Loading...</p>
    </div>
</div>

</template>