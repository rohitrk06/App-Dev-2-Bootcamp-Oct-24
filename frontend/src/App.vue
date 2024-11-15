<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { computed } from 'vue'
import { useMessageStore } from './stores/messageStore'
import { useAuthStore } from './stores/auth_store'

const authStore = useAuthStore()
const isAuthenticated = computed(() => authStore.isAuthenticated)


const messageStore = useMessageStore()
const message = computed(() => messageStore.getFlashMessage())
const user_details =JSON.parse(authStore.getUserDetails())
// const user_details =authStore.getUserDetails()

function logout() {
  //Fetch api to logout
  fetch(`${authStore.getBackendServerURL()}/api/v1/logout`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authentication-Token': authStore.getAuthToken(),
      'Acess-Control-Allow-Origin': '*'
    }
  }).then(response => response.json()).then(data => {
    messageStore.setFlashMessage(data.message)
  })  
  authStore.removeAuthenticatedUser()
  // messageStore.setFlashMessage('You have been logged out')
}

const isAdmin =  computed(()=>{
  // user_details = authStore.getUserDetails()
  if (isAuthenticated.value){
    console.log(user_details)
    if (user_details.roles.includes('admin')){
      return true
    }
  }
  return false
})

const isCustomer =  computed(()=>{
  if (isAuthenticated.value){
    if (user_details.roles.includes('customer')){
    return true
    } 
  }
  return false
})

const isStoreManager = computed(()=>{
  // user_details = authStore.getUserDetails()
  if (isAuthenticated.value){
    if (user_details.roles.includes('store_manager')){
    return true
  }
  } 
  return false
})

</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <RouterLink to="/" class="navbar-brand">Grocery Store</RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li v-if="!isAuthenticated" class="nav-item">
            <RouterLink to="/login" class="nav-link">Login</RouterLink>
          </li>
          <li class="nav-item" v-if="!isAuthenticated">
            <RouterLink to="/register" class="nav-link">Register</RouterLink>
          </li> 
          <li v-if="isAdmin" class="nav-item">
            <RouterLink to="/add_category" class="nav-link">Add Category</RouterLink>
          </li>
          <li v-if="isAuthenticated" class="nav-item">
            <RouterLink to="/" class="nav-link">{{user_details.username}}</RouterLink>
          </li>
          <li v-if="isAuthenticated" class="nav-item">
            <button @click="logout" class="nav-link">Logout</button>
          </li>       
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
  <div v-if="message" class = "container-fluid text-bg-primary p-2">
    <p>{{ message }}</p>
  </div>
  <RouterView />
</template>
