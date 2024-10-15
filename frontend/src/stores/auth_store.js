import {ref, computed} from 'vue'
import {defineStore} from 'pinia'

export const useAuthStore = defineStore('auth', () => {
    const backend_server = 'http://127.0.0.1:5000'

    function getToken(){
        return localStorage.getItem('token')
    }

    function getBackendServerURL(){
        return backend_server
    }


    return {
        getBackendServerURL
    }

})