<template>
    <div class="container-fluid mt-5">
        <h1 class="text-center">Add Product</h1>
        <form class="row justify-content-center" @submit.prevent = "add_product" >
            <div class="mb-3 col-7">
            <label for="name" class="form-label">Product Name</label>
            <input type="text" class="form-control" id="name" v-model="name" required>
            </div>
            <div class="mb-3 col-7">
            <label for="selling_price" class="form-label">Selling Price</label>
            <input type="text" class="form-control" id="selling_price" v-model="selling_price">
            </div>
            <div class="mb-3 col-7">
                <label for="cost_price" class="form-label">Cost Price</label>
                <input type="text" class="form-control" id="cost_price" v-model="cost_price">
            </div>
            <div class="mb-3 col-7">
                <label for="stock" class="form-label">Stock</label>
                <input type="number" class="form-control" id="stock" v-model="stock">
            </div>
            <div class="mb-3 col-7">
                <label for="mfg_date" class="form-label">Manufacturing Date</label>
                <input type="date" class="form-control" id="mfg_date" v-model="mfg_date">
            </div>
            <div class="mb-3 col-7">
                <label for="expiry_date" class="form-label">Expiry Date</label>
                <input type="date" class="form-control" id="expiry_date" v-model="expiry_date">
            </div>
            <div class="mb-3 col-7">
                <label for="category" class="form-label">Category</label>
                <select class="form-select" id="category" v-model="selected_category">
                        <option v-for="category in categories" value="{{category.category_id}}">{{category.category_name}}</option>
                </select>
            </div>
            <div class="col-7">
                <button  type="submit" class="btn btn-primary">Add Product</button>
            </div>

        </form>
    </div>
</template>


<script setup>

import { ref, computed, onMounted } from 'vue'; 
import { useMessageStore } from '@/stores/messageStore';
import { useAuthStore } from '@/stores/auth_store';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const messageStore = useMessageStore();

const backend_url = computed(() => authStore.getBackendServerURL());
const router = useRouter();

const categories = ref([]);

const name = ref('');
const selling_price = ref('');
const cost_price = ref('');
const stock = ref('');
const mfg_date = ref('');
const expiry_date = ref('');
const selected_category = ref('');


const fetch_categories = function(){
    fetch(
        `${backend_url.value}/api/v1/categories`,
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authentication-Token': authStore.getAuthToken(),
                'Acess-Control-Allow-Origin': '*'
            }
        }
    ).then(response => response.json()).then(data=>
        {
            // console.log(data);
            categories.value = data;
            console.log(categories.value);
        }
    )
}

onMounted(() =>{
    fetch_categories();
    }
)

const add_product = function(){
    // Create a fetch request to send the data to be added 
    // to backend using fetch apis
    // similar to adding the categories
}


</script>
