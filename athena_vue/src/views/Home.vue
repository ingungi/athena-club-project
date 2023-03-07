<template>
  
  <div class="home">
    
    <div class="carousel-container">
      <div class="carousel">
        <div class="slides" ref="slides">
          <div class="slide" v-for="(product, index) in products" :key="index">
            <ItemCard :id="product.id" />
          </div>
        </div>
        <div class="carousel-controls">
          <div class="prev" @click="prevSlide">&lt;</div>
          <div class="next" @click="nextSlide">&gt;</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ItemCard from './ItemCard.vue'
import FavouritesCard from './FavouritesCard.vue'


export default {
  name: 'Home',
  components: {
    ItemCard,
    FavouritesCard,

  },
  data() {
    return {
      products: [],
      currentSlide: 1,
      slideWidth: null,
      totalSlides: null,
      slideInterval: null,
    }
  },
  mounted() {
    this.slideWidth = this.$refs.slides.offsetWidth;
  },
  methods: {
    prevSlide() {
      if (this.currentSlide > 1) {
        this.currentSlide--;
        this.moveSlide();
      } else {
        this.currentSlide = this.totalSlides;
        this.moveSlide();
      }
    },
    nextSlide() {
      if (this.currentSlide < this.totalSlides) {
        this.currentSlide++;
        this.moveSlide();
      } else {
        this.currentSlide = 1;
        this.moveSlide();
      }
    },
    moveSlide() {
      let slidePosition = (this.currentSlide - 1) * -this.slideWidth;
      this.$refs.slides.style.transform = `translateX(${slidePosition}px)`;
    },
  },
  created() {
    console.log('Fetching products...')
    axios
      .get('/api/v1/carousel-products/')
      .then(response => {
        this.products = response.data
        this.totalSlides = this.products.length;
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 2rem;
  margin-top: 2rem;
}
.carousel-container {
  width: 70%;
  overflow: hidden;
}

.carousel {
  display: flex;
  flex-direction: row;
  position: relative;
}

.slides {
  display: flex;
  flex-direction: row;
  transition: transform 0.3s ease-in-out;
}

.slide {
  margin: 0 16px;
  width: 300px;
}

.carousel-controls {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.carousel-controls > div {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  font-size: 32px;
  font-weight: bold;
  background-color: rgba(0, 0, 0, 0.3);
  color: #fff;
  cursor: pointer;
  pointer-events: all;
  transition: background-color 0.3s ease-in-out;
}

.carousel-controls > div:hover {
  background-color: rgba(0, 0, 0, 0.5);
}

.carousel-controls > .prev {
  margin-right: auto;
}

.carousel-controls > .next {
  margin-left: auto;
}
</style>