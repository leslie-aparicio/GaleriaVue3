<template>
  <div class="carousel">
    <div v-if="images.length">
      <img :src="images[currentSlide]" class="slide" alt="Imagen del carrusel" />

      <!-- Navegación -->
      <div class="navigate">
        <div class="toggle-page left">
          <i @click="prevSlide" class="fas fa-chevron-left"></i>
        </div>
        <div class="toggle-page right">
          <i @click="nextSlide" class="fas fa-chevron-right"></i>
        </div>
      </div>

      <!-- Paginación -->
      <div class="pagination">
        <span v-for="(image, index) in images" :key="index" :class="{ active: index === currentSlide }">
          {{ index + 1 }}
        </span>
      </div>
    </div>
    <div v-else>Cargando imágenes...</div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  setup() {
    const images = ref([]);
    const currentSlide = ref(0);

    // Función para cargar imágenes desde la API
    const fetchImages = async () => {
      try {
        const response = await axios.get("http://localhost:8000/images");
        images.value = response.data.map(item => item.url);
      } catch (error) {
        console.error("Error al cargar imágenes:", error);
      }
    };

    const nextSlide = () => {
      currentSlide.value = (currentSlide.value + 1) % images.value.length;
    };

    const prevSlide = () => {
      currentSlide.value = (currentSlide.value - 1 + images.value.length) % images.value.length;
    };

    onMounted(fetchImages);

    return { images, currentSlide, nextSlide, prevSlide };
  }
};
</script>

<style lang="scss">
.carousel {
  text-align: center;
}
img {
  width: 100%;
  max-width: 600px;
  height: auto;
}
.navigate {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}
.toggle-page {
  cursor: pointer;
  font-size: 24px;
}
.pagination {
  margin-top: 10px;
}
.active {
  font-weight: bold;
}
</style>
