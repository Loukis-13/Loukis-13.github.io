<script setup>
import Linguagens from "./components/Linguagens.vue"
import Projetos from "./components/Projetos.vue"
import Certificacoes from "./components/Certificacoes.vue"

const redesSociais = [
    ["git.png", "https://github.com/Loukis-13"],
    ["linkedin.png", "https://www.linkedin.com/in/jose-nivaldo-da-silva-hypolito/"],
    ["replit.png", "https://replit.com/repls"],
    ["dio.png", "https://web.digitalinnovation.one/users/ze_zinho-2010?tab=achievements"],
    ["codingame.svg", "https://www.codingame.com/profile/ddb616fcb36cc5ab528b00c539d62bab8607605"],
    ["fcc.png", "https://www.freecodecamp.org/loukis"],
]
</script>

<template>
    <div class="grey lighten-2">
        <div class="bg-black pb-2">
            <div class="flex items-center justify-between">
                <div class="basis-2/3 lg:basis-1/2 grid grid-cols-6 gap-3 lg:gap-5 bg-neutral-400 rounded-br-3xl p-1">
                    <a v-for="[i, j] in redesSociais" :href="j" target="_blank">
                        <img class="p-1" :src="'/redes-sociais/'+i" />
                    </a>
                </div>
                <a class="me-3 hidden lg:block" href="https://www.codewars.com/users/Loukis" target="_blank"><img class="right" src="https://www.codewars.com/users/Loukis/badges/large"></a>
                <a class="me-3 block lg:hidden" href="https://www.codewars.com/users/Loukis" target="_blank"><img class="right" src="https://www.codewars.com/users/Loukis/badges/micro"></a>
            </div>

            <h1 class="text-white text-3xl lg:text-6xl mt-5 lg:my-8">JOSÉ NIVALDO DA SILVA HYPÓLITO</h1>
            <h2 class="text-white text-2xl lg:text-5xl my-2 lg:my-5">DESENVOLVEDOR</h2>
            <Linguagens />
        </div>

        <div class="row">
            <Projetos />

            <div class="bg-neutral-900 text-neutral-400 p-3">
                <h2 class="white-text text-5xl m-6">CERTIFICAÇÕES</h2>
                <Certificacoes />
            </div>
        </div>
    </div>
</template>

<style>
@font-face {
    font-family: "KoHo";
    src: url("@/assets/KoHo/KoHo-Regular.ttf");
}

body {
    text-align: center;
    font-family: 'KoHo', sans-serif;
}

h5 {
    white-space: pre-line;
}

code {
    white-space: pre-line;
}
</style>
