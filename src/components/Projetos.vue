<script setup>
import { ref, onMounted } from 'vue'
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import Projeto from '@/components/Projeto.vue'

// DEMONSTRAÇÕES DE SQL
import queries from '@/assets/SQL_queries.json'
let query = ref(0);

// DEMONSTAÇÕES DE ANÁLISE DE DADOS
const urlDados = {
    mvs: 'https://colab.research.google.com/drive/1XqWO1akL_v2Rvve8x1E-qQqvRqnI3kxy?usp=sharing',
    medicalData: 'https://colab.research.google.com/drive/1gabe6Tdy0SfPBIpHG1_FJ0168imXz7h1?usp=sharing',
    demographic: 'https://colab.research.google.com/drive/1z-AFWAm185-hAy_kAYYNYAuRvFu-9cE_?usp=sharing',
    pageView: 'https://colab.research.google.com/drive/11qkOfJlo-8JKne7wPtd39xVINqLYS-vJ?usp=sharing',
    seaLevel: 'https://colab.research.google.com/drive/17_eYVYndSfQ5lVeltbytLF2NbBtMluyM?usp=sharing'
}
let dados = ref(urlDados.mvs)

// CONWAY'S GAME OF LIFE
import PlayIcon from '@/assets/icons/play_arrow.svg'
import RestartIcon from '@/assets/icons/restart.svg'
import ClearIcon from '@/assets/icons/clear.svg'
onMounted(() => {
    import('@/assets/game_of_life/index.js')
})
const conwayGameOfLifeFps = ref(10);
</script>

<template>
    <!-- <Projeto
        nome=""
        foto=""
        repositorio=""
        pagina=""
        :linguagens="[]"
    >
    </Projeto> -->

    <Projeto 
        nome="DUNGEON RAIDERS" 
        foto="/projetos/dungeon/tela1.png"
        repositorio="https://github.com/Loukis-13/Dungeon-Raiders-Phaser"
        pagina="https://loukis-13.github.io/Dungeon-Raiders-Phaser/"
        :linguagens="['Javascript']"
    >
        <i18n-t keypath="dungeonRaiders.description">
            <a class="text-blue-500" href="https://www.ludopedia.com.br/jogo/dungeon-raiders" target="_blank">Dungeon Raiders</a>
        </i18n-t>
        <br />
        <br />
        <a class="text-blue-500" href="https://loukis-13.github.io/Dungeon-Raiders-Phaser/" target="_blank">
            {{ $t("dungeonRaiders.play") }}
        </a>
    </Projeto>

    <Projeto 
        nome="ESTE SITE" 
        foto="/projetos/portfolio.png"
        repositorio="https://github.com/Loukis-13/Loukis-13.github.io"
        :linguagens="['Javascript', 'Node', 'Vue', 'Vitejs', 'Tailwind']"
    >
        {{ $t("thisSite.description") }} <a class="text-blue-500" href="https://vuejs.org/" target="_blank">Vue.js</a>.
    </Projeto>

    <Projeto 
        nome="NES EMULATOR IN RUST" 
        foto="/projetos/emulador-nes/Ferris NES.png"
        repositorio="https://github.com/Loukis-13/NES-emulator-in-Rust"
        :linguagens="['Rust']"
    >
        <i18n-t keypath="nesEmulatorInRust.description">
            <a class="text-blue-500" href="https://bugzmanov.github.io/nes_ebook/chapter_1.html" target="_blank">NES Ebook</a>
        </i18n-t>
    </Projeto>

    <Projeto 
        nome="RAY TRACING IN ONE WEEKEND" 
        foto="https://github.com/Loukis-13/ray-tracing-in-one-weekend/blob/master/images/spheres-0.png?raw=true"
        repositorio="https://github.com/Loukis-13/ray-tracing-in-one-weekend"
        :linguagens="['Rust']"
    >
        <i18n-t keypath="rayTracingInOneWeekend.description">
            <a class="text-blue-500" href="https://raytracing.github.io/books/RayTracingInOneWeekend.html" target="_blank">Ray Tracing in One Weekend</a>
        </i18n-t>
    </Projeto>

    <Projeto 
        nome="CONWAY'S GAME OF LIFE"
        repositorio="https://github.com/Loukis-13/Loukis-13.github.io/blob/276282ddbbebd499f7068b69753b4bf3037c7b48/src/components/Projetos.vue#L21"
        :linguagens="['Javascript', 'Rust', 'WebAssembly']"
    >
        <template v-slot:imagem>
            <canvas id="game-of-life-canvas" class="aspect-video w-full"></canvas>
            <div class="flex justify-between items-center">
                <div class="flex justify-between w-1/2">
                    <p>FPS</p>
                    <input id="fps-control" type="range" min="10" max="60" v-model="conwayGameOfLifeFps">
                    <p>{{ conwayGameOfLifeFps }}</p>
                </div>
                
                <div class="flex justify-around w-1/2 px-8">
                    <img id="play-pause" class="cursor-pointer aspect-square" :src="PlayIcon">
                    <img id="restart" class="cursor-pointer aspect-square" :src="RestartIcon">
                    <img id="kill-all" class="cursor-pointer aspect-square" :src="ClearIcon">
                </div>
            </div>
        </template>

        <i18n-t keypath="conwaysGameOfLife.description">
            <a class="text-blue-500" href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Conway's Game of Life</a>
        </i18n-t>
    </Projeto>

    <Projeto 
        nome="RSA® IMPLEMENTATIONS" 
        foto="/projetos/rsa.png"
        repositorio="https://github.com/Loukis-13/RSA-implementations"
        :linguagens="['Python', 'Rust']"
    >
        {{ $t("rsaImplementations.description") }}
    </Projeto>

    <Projeto 
        nome="FOREX TRADING" 
        foto="/projetos/forex-trading/forex-trading.png"
        repositorio="https://github.com/Loukis-13/Forex-Trading"
        pagina="https://loukis-13.github.io/Forex-Trading/"
        :linguagens="['Javascript', 'Node', 'React', 'Nextjs', 'Tailwind']"
    >
        <i18n-t keypath="forexTrading.description">
            <a class="text-blue-500" href="https://exchangerate.host/" target="_blank">exchangerate.host</a>
        </i18n-t>
    </Projeto>

    <Projeto 
        nome="INTERFATECS" 
        foto="/projetos/InterFatecs.png"
        repositorio="https://github.com/Loukis-13/InterFatecs"
        :linguagens="['Python']"
    >
        <i18n-t keypath="interfatecs.description">
            <a class="text-blue-500" href="https://interfatecs.com.br/" target="_blank">InterFatecs</a>
        </i18n-t>
    </Projeto>

    <Projeto 
        nome="DEMONSTRAÇÕES DE SQL"
        :linguagens="['PostgreSQL', 'SQLite']"
    >
        <template v-slot:imagem> 
            <div v-for="(v, i) in queries">
                <a v-show="i == query" class="text-3xl lg:text-4xl mb-2 text-blue-500 hover:underline" :href="v.link" target="_blank">{{ v.name }}</a>
                <pre v-show="i == query" class="w-full aspect-video"><code class="language-sql">{{ v.query }}</code></pre>
            </div>
        </template>

        {{ $t("sqlDemonstrations.description") }}
        <br />
        <select class="border border-gray-300 text-gray-900 block w-full p-2" v-model="query">
            <option v-for="(v, i) in queries" :value="i">{{ v.name }}</option>
        </select>
    </Projeto>

    <Projeto 
        nome="RGit" 
        foto="/projetos/rgit/rgit.png"
        repositorio="https://github.com/Loukis-13/RGit"
        :linguagens="['Ruby']"
    >
        {{ $t("rgit.description") }}
    </Projeto>

    <Projeto 
        nome="DESAFIO FULLSTACK SIFAT" 
        foto="/projetos/desafio-sifat/demo.webp"
        repositorio="https://github.com/Loukis-13/desafio-fullstack-sifat"
        :linguagens="['Python', 'Javascript', 'Vue']"
    >
        {{ $t("desafioFullstackSifat.description") }}
    </Projeto>

    <Projeto 
        nome="MUSICAL" 
        foto="/projetos/musical/musical.png"
        repositorio="https://github.com/Loukis-13/musical-kotlin"
        :linguagens="['Java', 'Kotlin', 'Docker', 'Kafka']"
    >
        {{ $t("musical.description") }}
        <br/>
        <br/>
        <a class="text-blue-500" href="https://github.com/Loukis-13/musical">{{ $t("musical.versionInJava") }}</a>
    </Projeto>

    <Projeto 
        nome="CURRENCY API" 
        foto="/projetos/go-currency-api/go-currency-api.png"
        repositorio="https://github.com/Loukis-13/currency-API-GO"
        :linguagens="['GO', 'MongoDB']"
    >
        {{ $t("currencyApi.description") }}
    </Projeto>

    <Projeto 
        nome="DEMONSTAÇÕES DE ANÁLISE DE DADOS" 
        foto="/projetos/analise-de-dados/graficos.png"
        repositorio="https://github.com/Loukis-13/FCC_analise_de_dados" 
        :linguagens="['Python']"
    >
        {{ $t("dataAnalisysDemonstrations.description") }}
        <br />
        <br />
        <div>
            <select v-model="dados" class="border border-gray-300 text-gray-900 block w-full p-2">
                <option :value="urlDados.mvs">Mean Variance Standard-deviation Calculator</option>
                <option :value="urlDados.medicalData">Medical Data Visualizer</option>
                <option :value="urlDados.demographic">Demographic Data Analyzer</option>
                <option :value="urlDados.pageView">Page View Time Series Visualizer</option>
                <option :value="urlDados.seaLevel">Sea Level Predictor</option>
            </select>
            <br />
            <a class="bg-gray-600 p-2 rounded text-white" :href="dados" target="_blank">ABRIR</a>
        </div>
    </Projeto>

    <Projeto 
        nome="BACKEND DEVELOPMENT AND APIs" 
        foto="/projetos/FCC_APIs/fcc-apis.png"
        repositorio="https://github.com/Loukis-13/FCC_APIs"
        :linguagens="['Node']"
    >
        {{ $t("backendDevepmentAndApis.description") }}
        <!-- Escritas Node.js e implementadas na plataforma do Heroku, todas as APIs foram reunidas em um único app para melhor manueseio. -->
    </Projeto>

    <Projeto 
        nome="NOSSA CANTINA"
        repositorio="https://github.com/Loukis-13/nossa-cantina"
        :linguagens="['Python', 'Javascript', 'MySQL']"
    >
        <template v-slot:imagem>
            <Splide :options="{type: 'loop'}" class="w-full">
                <SplideSlide v-for="i in '123456'" class="w-full flex items-center">
                    <img :src="`/projetos/nossa-cantina/${i}.png`" />
                </SplideSlide>
            </Splide>
        </template>

        {{ $t("nossaCantina.description") }}
    </Projeto>

    <Projeto 
        nome="LEITOR ÁGIL" 
        foto="/projetos/leitor/leitor.png"
        repositorio="https://github.com/Loukis-13/leitor_agil"
        :linguagens="['Flutter', 'Dart']"
    >
        {{ $t("agileReader.description") }}
        <br/>
        <br/>
        <a class="text-blue-500" href="https://github.com/Loukis-13/Leitor-agil" target="_blank">{{ $t("agileReader.versionInPython") }}</a>
    </Projeto>

    <!-- <Projeto 
        nome="GESSO MORRO AGUDO" 
        foto="/projetos/gesso/gesso.png"
        repositorio="https://github.com/Loukis-13/gesso-morro-agudo"
        pagina="https://loukis-13.github.io/gesso-morro-agudo/"
        :linguagens="['Python', 'Javascript']"
    >
        Catálogo simples que extrai os dados de um csv<br/>
    </Projeto> -->

    <Projeto 
        nome="FRASES CÔMICAS DOS PRESIDENTES" 
        foto="/projetos/frases-comicas-dos-presidentes/frases-comicas-dos-presidentes.png"
        repositorio="https://github.com/Loukis-13/frases_presidentes"
        pagina="https://loukis-13.github.io/frases_presidentes/"
        :linguagens="['Python']"
    >
        {{ $t("frasesComicasDosPresidentes.description") }}
    </Projeto>
</template>
