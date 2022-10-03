<script setup>
import Linguagens from "./components/Linguagens.vue"
import Projetos from "./components/Projetos.vue"
import Certificados from "./components/Certificados.vue"

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
        <div class="black" style="padding-bottom: 1% !important;">
            <div class="row valign-wrapper">
                <div class="col l5 m8">
                    <div class="row grey" style="border-bottom-right-radius: 3vw;">
                        <a v-for="[i, j] in redesSociais" class="col s2" :href="j" target="_blank">
                            <img class="responsive-img" :src="'img/redes-sociais/'+i" style="height: ; padding: 2%;">
                        </a>
                    </div>
                </div>
                <a class="col l7 m4 hide-on-med-and-down" href="https://www.codewars.com/users/Loukis" target="_blank"><img class="right" src="https://www.codewars.com/users/Loukis/badges/large"></a>
                <a class="col l7 m4 hide-on-large-only" href="https://www.codewars.com/users/Loukis" target="_blank"><img class="right" src="https://www.codewars.com/users/Loukis/badges/micro"></a>
            </div>

            <h1 class="white-text" style="margin-top: 0;">JOSÉ NIVALDO DA SILVA HYPÓLITO</h1>
            <h2 class="white-text">DESENVOLVEDOR</h2>
            <Linguagens />
        </div>

        <div class="row" style="margin-bottom: 0;">
            <Projetos />

            <div class="col s12 grey darken-4" style="padding-bottom: 3%;">
                <h2 class="white-text" style="margin: 3% 0;">CERTIFICAÇÕES</h2>
                <Certificados />
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

.m-1 {
    margin: 1% !important;
}

@media only screen and (max-width: 600px) {
    h1 {
        font-size: 10vw;
    }

    h2 {
        font-size: 9vw;
    }
}
</style>
