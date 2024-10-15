<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { computed } from 'vue'
import { useMessageStore } from './stores/messageStore'


const messageStore = useMessageStore()
const message = computed(() => messageStore.getFlashMessage())

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
          <li class="nav-item">
            <RouterLink to="/login" class="nav-link">Login</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/register" class="nav-link">Register</RouterLink>
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
