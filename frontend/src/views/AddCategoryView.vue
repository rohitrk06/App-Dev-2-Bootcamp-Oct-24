<script setup>
import { ref, computed } from 'vue'; 
import { useMessageStore } from '@/stores/messageStore';
import { useAuthStore } from '@/stores/auth_store';
import { useRouter } from 'vue-router';
const authStore = useAuthStore();
const messageStore = useMessageStore();

const backend_url = computed(() => authStore.getBackendServerURL());
const router = useRouter();

const category_name = ref('');
const description = ref('');

function add_category(){
    const input_data={
        'category_name': category_name.value,
        'category_description': description.value
    }
    fetch(
        `${backend_url.value}/api/v1/category`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authentication-Token': authStore.getAuthToken(),
                'Acess-Control-Allow-Origin': '*'
            },
            body: JSON.stringify(input_data)
        }
    ).then(response => response.json()).then(data=>
        {
            messageStore.setFlashMessage(data.message);
        }
    )
    router.push('/');
}



</script>
<template>

<div class = "container-fluid col-8 align-center">
    <h1 class="text-center m-3">Add Category</h1>
    <form @submit.prevent="add_category">
        <div class="mb-3">
            <label for="category_name" class="form-label">Category Name</label>
            <input type="text" class="form-control" id="category_name" v-model="category_name" required>
        </div>
        <div class="mb-3">
            <label for="description" class="form-label">Description</label>
            <textarea class="form-control" id="description" v-model="description" rows="3" placeholder="Description"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Add Category</button>
    </form>
</div>

</template>