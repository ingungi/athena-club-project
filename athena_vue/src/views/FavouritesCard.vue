<template>
  <div class="circular-component">
    <h2 class="component-heading">Meet the Favorites</h2>
  </div>
</template>

<style>
.circular-component {
    font-family: 'brown-regular-webfont';
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background-color: #e9f5fa;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.component-heading {
  text-decoration: none;
    color: #004495;
    background: #e9f5fa;
    text-align: center;
    border-radius: 50%;
    display: block;
    max-width: 325px;
    position: relative;
    margin-top: 39px;
}
.circular-sm {
  width: 50px;
  height: 50px;
  line-height: 50px;
  font-size: 18px;
  border-radius: 50%;
  background-color: #FFB14D;
  color: #fff;
  text-align: center;
  margin-right: 10px;
}
@font-face {
  font-family: 'brown-regular-webfont';
  src: url('/Users/ianngungi/Desktop/athena-club-project/athena_vue/src/assets/brown-regular-webfont.woff') format('woff');
}
</style>
