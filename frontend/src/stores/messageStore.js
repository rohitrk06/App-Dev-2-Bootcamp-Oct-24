import {ref, computed} from 'vue'
import {defineStore} from 'pinia'

export const useMessageStore = defineStore('auth', () => {
    const flash_message = ref('')

    function setFlashMessage(message){
        flash_message.value = message
        setTimeout(() => {
            flash_message.value = ''
        }, 5000)
    }

    function getFlashMessage(){
        return flash_message.value
    }

    return {
        setFlashMessage,
        getFlashMessage
    }
})