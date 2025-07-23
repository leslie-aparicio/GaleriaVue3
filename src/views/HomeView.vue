<template>
  <div class="home">
    <Carousel class="carousel">
      <Slide v-for="(image, index) in images" :key="index">
        <div v-show="currentSlide === index" class="slide-info">
          <!-- Usar la URL de la imagen obtenida desde la API -->
          <img :src="image" alt="Imagen del carrusel" />
        </div>
      </Slide>
    </Carousel>

    <!-- Botones de navegación -->
    <div class="navigation">
      <button @click="prevSlide">Anterior</button>
      <button @click="nextSlide">Siguiente</button>
    </div>
  </div>
</template>

<script>
import Carousel from '../components/CarouselWrapper.vue';
import Slide from '../components/SlideWrapper.vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'HomeView',
  components: { Carousel, Slide },
  setup() {
    const images = ref([]);
    const currentSlide = ref(0);

    // Cargar imágenes desde la API
    const fetchImages = async () => {
      try {
        const response = await axios.get('http://localhost:8000/images');
        // Las imágenes ya tienen la URL completa
        images.value = response.data.map(item => item.url);
      } catch (error) {
        console.error('Error al cargar imágenes:', error);
      }
    };

    // Función para pasar al siguiente slide
    const nextSlide = () => {
      currentSlide.value = (currentSlide.value + 1) % images.value.length;
    };

    // Función para ir al slide anterior
    const prevSlide = () => {
      currentSlide.value = (currentSlide.value - 1 + images.value.length) % images.value.length;
    };

    onMounted(fetchImages);

    return { images, currentSlide, nextSlide, prevSlide };
  }
}
</script>

<style lang="scss" scoped>
.carousel {
  position: relative;
  max-height: 100vh;
  height: 100vh;

  .slide-info {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    max-height: 100%;
    height: 100%;

    img {
      min-width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
}

.navigation {
  text-align: center;
  margin-top: 20px;
}

button {
  padding: 10px;
  margin: 0 5px;
  font-size: 16px;
  cursor: pointer;
}
</style>
