<template>
  <div>
    <b-alert variant="success" show>{{ message }}</b-alert>
  </div>
</template>

<script>
export default {
  name: 'alert-component',
  props: ['message'],
};
</script>
