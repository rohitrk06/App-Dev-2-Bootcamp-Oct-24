<script setup>
import TheWelcome from '../components/TheWelcome.vue'
import Category from '../components/Category.vue'

import { ref, computed, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth_store';

const authStore = useAuthStore();

const backend_url = computed(() => authStore.getBackendServerURL());

const categories = ref([]);
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

onMounted(() => {
  console.log('HomeView mounted')

  fetch_categories()
})

</script>

<template>
  <main>
    <Category v-for="category in categories" :category_id="category.category_id" />
  </main>
</template>
