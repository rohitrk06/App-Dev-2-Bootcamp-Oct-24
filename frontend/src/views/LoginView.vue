<script setup>

import { computed, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useMessageStore } from '@/stores/messageStore';
import { useAuthStore } from '@/stores/auth_store';

const password = ref('');
const username = ref('');


const router = useRouter();
const route = useRoute();

const category_id = ref(route.params.id);

const messageStore = useMessageStore();
const authStore = useAuthStore();

const backend_url = computed(() => authStore.getBackendServerURL());

async function login() {
    const input_data = {
        username: username.value,
        password: password.value
    }
    console.log(input_data);    
    
    const response = await fetch(`${backend_url.value}/api/v1/login`,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Acess-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(input_data)
    })
    if (response.ok){
        const data = await response.json();
        console.log(data);
        messageStore.setFlashMessage(data.message);
        // localStorage.setItem('auth_token', data.login_credentials.auth_token);
        authStore.setAuthToken(data.login_credentials.auth_token);
        const user_details = {
            username: data.login_credentials.username,
            roles: data.login_credentials.roles
        }
        // localStorage.setItem('user_details', JSON.stringify(user_details));
        authStore.setUserDetails(user_details);
        // redirect to home page
        router.push('/');
    }
    else{
        const data = await response.json();
        messageStore.setFlashMessage(data.message);
    }

}

</script>

<template>
    <div class="container-fluid mt-2 p-3">
        <h1 class="text-center">Login</h1>
        <div class="d-flex justify-content-center">
            <form class="w-50 justify-content-center" @submit.prevent="login">
                <div class="mb-3">
                    <label for="username" class="form-label">username</label>
                    <input type="text" class="form-control" id="username" v-model="username">
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Password</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
                </div>
                <div class="d-flex justify-content-center mb-3">
                    <button type="submit" class="btn btn-primary">Login</button>
                </div>
                <div class="d-flex justify-content-center mt-2">
                    <span>Don't have an account? &ensp; </span>
                    <RouterLink to='/register'>Register</RouterLink>
                </div>
            </form>
        </div>  
    </div>
</template>