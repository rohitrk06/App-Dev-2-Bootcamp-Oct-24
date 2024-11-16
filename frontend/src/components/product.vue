<script setup>

import { ref, computed, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth_store';
import { useMessageStore } from '@/stores/messageStore';

const props = defineProps({
    product_id : {
        type: Number,
        required: true
    }
})

</script>


<template>
    <div>
        <h1>Product</h1>
        {{ props.product_id }}
    </div>
</template>