<template>
  <div class="star-rating">
    <span v-for="i in maxStars" :key="i" class="star" :class="{ filled: i <= rating }">&#9733;</span>
    <span v-if="showRating" class="rating">{{ rating }} / {{ maxStars }}</span>
  </div>
</template>

<script>
export default {
  props: {
    rating: {
      type: Number,
      required: true
    },
    maxStars: {
      type: Number,
      default: 5
    },
    showRating: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped>
.star-rating {
  display: inline-flex;
  align-items: center;
}

.star {
  color: #004495;
  font-size: 24px;
}

.star.filled {
  color: #004495;
}

.rating {
  margin-left: 8px;
  font-size: 16px;
  font-weight: bold;
  color: #888;
}
</style>
