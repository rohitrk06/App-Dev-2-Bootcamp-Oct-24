<script setup>

import { computed, ref } from 'vue';
import { useMessageStore } from '@/stores/messageStore';
import { useAuthStore } from '@/stores/authStore';

const password = ref('');
const email = ref('');

const messageStore = useMessageStore();
const authStore = useAuthStore();

const backend_url = computed(() => authStore.getBackendServerURL());

async function login() {
    const input_data = {
        email: email.value,
        password: password.value
    }
    console.log(input_data);    
    
    const response = await fetch(`${backend_url}/api/v1/login`,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Acess-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(input_data)
    })
    console.log(response);

}

</script>

<template>
    <div class="container-fluid mt-2 p-3">
        <h1 class="text-center">Login</h1>
        <div class="d-flex justify-content-center">
            <form class="w-50 justify-content-center" @submit.prevent="login">
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Email address</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" v-model="email">
                    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
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