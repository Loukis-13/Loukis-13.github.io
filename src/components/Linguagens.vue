<script setup>
import { Splide, SplideTrack, SplideSlide } from '@splidejs/vue-splide';
import { AutoScroll } from '@splidejs/splide-extension-auto-scroll';

const lista_linguagens = ["Java", "Kotlin", "Rust", "Python", "Javascript", "TypeScript", "GO", "Lua", "Dart", "Ruby", "Bash", "C", "C++", "C#", "BrainFuck", "Clojure", "jq", "AWK"]

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
  <Splide :options="options" :extensions="{ AutoScroll }" :has-track="false" class="langs mx-10 lg:mx-16">
    <SplideTrack class="flex items-center justify-between">
      <SplideSlide v-for="l in lista_linguagens" class="flex items-center p-2">
        <img :src="`/logos/${l=='C#' ? 'CS' : l}.svg`" class="w-full" :alt="l" :title="l" />
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
