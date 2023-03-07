<template>
  <div v-if="product">
    <div class="item-card">
      <div class="item-details">
        <h2 class="item-name">{{ product.name }} | ${{ product.price }}</h2>
        <p class="item-description">{{ product.description }}</p>
        <div class="item-rating">
          <star-rating :rating=parseFloat(product.rating)></star-rating>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from './StarRating.vue';

export default {
  name: 'ItemCard',
  components: {
    StarRating,
  },
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      product: null
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      try {
        const response = await axios.get(`/api/v1/products/?id=${this.id}`);
        this.product = response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.item-card {
  font-family: 'brown-regular-webfont2';
  display: inline-flex;
  flex-direction: column;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 24px;
  color: #004495;
  align-content: center;
  text-align: center;
}

.item-image {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
}

.item-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.item-info {
  padding: 16px;
}

.item-info h2 {
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 24px;
}

.item-description {
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 16px;
}

.item-price {
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 18px;
  font-weight: bold;
}
@font-face {
  font-family: 'brown-regular-webfont';
  src: url('/Users/ianngungi/Desktop/athena-club-project/athena_vue/src/assets/brown-regular-webfont.woff') format('woff');
}
@font-face {
  font-family: 'brown-regular-webfont2';
  src: url('/Users/ianngungi/Desktop/athena-club-project/athena_vue/src/assets/brown-regular-webfont.woff2') format('woff');
}
</style>

