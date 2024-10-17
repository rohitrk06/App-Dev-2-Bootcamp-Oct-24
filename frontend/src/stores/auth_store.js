import {ref, computed} from 'vue'
import {defineStore} from 'pinia'

export const useAuthStore = defineStore('auth', () => {
    const backend_server = 'http://127.0.0.1:5000'

    const token = ref(computed(() => localStorage.getItem('auth_token')))
    const user_details = ref(computed(() => localStorage.getItem('user_details')))

    const isAuthenticated = computed(() => {
        return token.value !== null
    })

    function getAuthToken(){
        return token.value
    }

    function getUserDetails(){
        return user_details.value
    }

    function getBackendServerURL(){
        return backend_server
    }

    return {
        getBackendServerURL,
        isAuthenticated,
        getAuthToken,
        getUserDetails
    }

})