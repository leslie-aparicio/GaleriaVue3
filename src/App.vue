<template>
  <div id="app">
    <Carrusel />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import Carrusel from './components/CarruselWrapper.vue'; // Asegúrate de que la ruta sea correcta

export default defineComponent({
  name: 'App',
  components: {
    Carrusel // Registramos el componente
  }
});
</script>
