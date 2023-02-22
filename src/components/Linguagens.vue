<script setup>
import { Splide, SplideTrack, SplideSlide } from '@splidejs/vue-splide';
import { AutoScroll } from '@splidejs/splide-extension-auto-scroll';

const lista_linguagens = ["Java", "Kotlin", "Rust", "Python", "Javascript", "TypeScript", "GO", "Lua", "Dart", "Ruby", "Bash", "C", "C++", "C#", "BrainFuck"]

const options = {
  type: 'loop',
  drag: 'free',
  perPage: 10,
  arrows: false,
  pagination: false,
  autoScroll: {
    speed: 1,
  },
}
</script>

<template>
  <Splide :options="options" :extensions="{ AutoScroll }" :has-track="false" class="langs" style="margin: 0 5%;">
    <SplideTrack class="row" style="display: flex;align-items: center;">
      <SplideSlide v-for="l in lista_linguagens" class="col l1 s2" style="display: flex; align-items: center;">
        <img :src="`img/logos/${l=='C#' ? 'CS' : l}.svg`" :alt="l" :title="l" style="max-width: 100%; width: 100%; margin: 0;" />
      </SplideSlide>
    </SplideTrack>
  </Splide>
</template>

<style scoped>
.langs:after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  background: linear-gradient(to right, black, transparent, transparent, transparent, black);
}
</style>
