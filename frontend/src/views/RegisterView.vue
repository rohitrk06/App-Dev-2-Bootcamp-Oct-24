<script setup>
import { computed, ref } from 'vue';
import { useMessageStore } from '@/stores/messageStore';
import { useAuthStore } from '@/stores/auth_store';

const authStore = useAuthStore();
const messageStore = useMessageStore();
const backend_url = computed(() => authStore.getBackendServerURL());
const username = ref('');
const email = ref('');
const password = ref('');
const confirm_password = ref('');
const address = ref('');
const role = ref('');

const password_match = computed(() => password.value === confirm_password.value);

const UsernameAvailability = ref('');
function checkUsernameAvailability(){
    // let result = None
    const input_data = {
        username: username.value,
    }
    fetch(`${backend_url.value}/api/v1/verify_user`,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Acess-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(input_data)
    }).then(
        response =>  response.json()
    ).then(
        (data) => {
            UsernameAvailability.value = data.message;
            // console.log(data);
            // result = data.message;
        }
    )
    // return result;
}


// Promise(resolve,reject).then(1st argument,2nd argument)

function register(){
    // you can do the validation here first
    // after validations, send the api request
    // handle the response from the api
}


watch(username,async (newVal,oldVal) => {
    if (newVal.length > 0){
        fetch()
    }
})


</script>

<template>
    <div class="container-fluid mt-2 p-3">
        <h1 class="text-center">Register</h1>
        <div class="d-flex justify-content-center">
            <form class="w-50 justify-content-center" @submit.prevent = 'register'>
                <div class="mb-3">
                    <label for="username" class="form-label"><strong>Username</strong></label>
                    <!-- <input type="text" class="form-control" id="username" aria-describedby="usernameHelp" v-model="username" @keyup="checkUsernameAvailability" required> -->
                    <input type="text" class="form-control" id="username" aria-describedby="usernameHelp" v-model="username" required>
                    <div id="usernameHelp" class="form-text">{{UsernameAvailability}}</div>
                </div>
                <div class="mb-3">
                <label for="email" class="form-label"><strong>Email Address</strong></label>
                <input type="email" class="form-control" id="email" v-model="email" required >
                </div>
                <div class="row">
                <div class="mb-3 col-6">
                    <label for="exampleInputPassword1" class="form-label"><strong>Password</strong></label>
                    <input type="password" class="form-control" id="exampleInputPassword1" v-model='password' required>
                </div>
                <div class="mb-3 col-6">
                    <label for="exampleInputPassword2" class="form-label"><strong>Confirm Password</strong> </label>
                    <input type="password" class="form-control" id="exampleInputPassword2" v-model = 'confirm_password' required>
                </div>
                <p v-if="!password_match">Passwords doesn't match. Please enter correct password</p>
                </div>
                <div class="mb-3">
                    <label for="address" class="form-label"><strong>Address</strong></label>
                    <textarea type="" class="form-control" id="address" v-model="address"></textarea>
                </div>
                <div class="mb-3">
                    <label for="phone" class="form-label"><strong>Role</strong></label>
                    <div class="input-group d-flex align-center">
                    <input type="radio" id="storemanager" v-model="role" value="store_manager" required>&ensp;
                    <label for="storemanager"> Store Manager </label>&ensp; &ensp;
                    <input type="radio" id="customer" v-model="role" value="customer" required>&ensp;
                    <label for="customer">Customer</label>
                    </div>
                </div>
                <div class="d-flex justify-content-center mb-3">
                    <button type="submit" class="btn btn-primary">Register</button>
                </div>
                <div class="d-flex justify-content-center mt-2">
                    <span>Alreay an existing user? &ensp; </span>
                    <RouterLink to="/login">Login</RouterLink>
                </div>
            </form>
        </div>  
    </div>    
</template>