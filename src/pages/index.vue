<template>
</template>
<script setup>

import router from '../router';
import {UserName} from '../main';
if(!UserName) {
  router.push('/login');
}else if(UserName === '') {
  router.push('/login');
}else{
  router.push('/welcome');
}

</script>