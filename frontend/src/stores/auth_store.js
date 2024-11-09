import {ref, computed} from 'vue'
import {defineStore} from 'pinia'

export const useAuthStore = defineStore('auth', () => {
    const backend_server = 'http://127.0.0.1:5000'

    const token = ref(localStorage.getItem('auth_token'))
    const user_details = ref(localStorage.getItem('user_details'))

    // token = {value: {user_details}}

    const isAuthenticated = computed(() => {
        return token.value !== null
    })

    function getAuthToken(){
        return token.value
    }

    function getUserDetails(){
        return user_details.value
    }

    function setAuthToken(new_token){
        token.value = new_token
        localStorage.setItem('auth_token', new_token)
    }

    function setUserDetails(new_user_details){
        user_details.value = new_user_details
        localStorage.setItem('user_details', JSON.stringify(new_user_details))
    }

    function removeAuthenticatedUser(){
        localStorage.removeItem('auth_token')
        localStorage.removeItem('user_details')
        token.value = null
        user_details.value = null
    }

    function getBackendServerURL(){
        return backend_server
    }

    return {
        getBackendServerURL,
        isAuthenticated,
        getAuthToken,
        getUserDetails,
        setAuthToken,
        setUserDetails,
        removeAuthenticatedUser
    }

})