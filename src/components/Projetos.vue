<script setup>
import { ref } from 'vue'
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import Projeto from '@/components/Projeto.vue'

import queries from '@/assets/SQL_queries.json'
let query = ref(0);

const url_dados = {
    mvs: 'https://colab.research.google.com/drive/1XqWO1akL_v2Rvve8x1E-qQqvRqnI3kxy?usp=sharing',
    medical_data: 'https://colab.research.google.com/drive/1gabe6Tdy0SfPBIpHG1_FJ0168imXz7h1?usp=sharing',
    demographic: 'https://colab.research.google.com/drive/1z-AFWAm185-hAy_kAYYNYAuRvFu-9cE_?usp=sharing',
    page_view: 'https://colab.research.google.com/drive/11qkOfJlo-8JKne7wPtd39xVINqLYS-vJ?usp=sharing',
    sea_level: 'https://colab.research.google.com/drive/17_eYVYndSfQ5lVeltbytLF2NbBtMluyM?usp=sharing'
}
let dados = ref(url_dados.mvs)
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
        Jogo digital criado com base no jogo de cartas <a class="text-blue-500" href="https://www.ludopedia.com.br/jogo/dungeon-raiders" target="_blank">Dungeon Raiders</a>.<br />
        Inicialmente feito utilizando Kivy para Python e depois migrado para Phaser 3.<br />
        Versão para um jogador terminada, versão para dois jogadores em desenvolvimento.<br />
        <br />
        <a class="text-blue-500" href="https://loukis-13.github.io/Dungeon-Raiders-Phaser/" target="_blank">JOGAR</a>
    </Projeto>

    <Projeto 
        nome="ESTE SITE" 
        foto="/projetos/portfolio.png"
        repositorio="https://github.com/Loukis-13/Loukis-13.github.io"
        :linguagens="['Javascript', 'Node', 'Vue', 'Vitejs', 'Tailwind']"
    >
        Meu espaço pessoal para expor meus projetos.<br/>
        Feito com <a class="text-blue-500" href="https://vuejs.org/" target="_blank">Vue.js</a>.
    </Projeto>

    <Projeto 
        nome="NES emulator in Rust" 
        foto="/projetos/emulador-nes/Ferris NES.png"
        repositorio="https://github.com/Loukis-13/NES-emulator-in-Rust"
        :linguagens="['Rust']"
    >
        Emulador do vide-game NES (Nintendo Entertainment System) escrito em Rust<br/>
        Desenvolvido com base no conteúdo do livro <a class="text-blue-500" href="https://bugzmanov.github.io/nes_ebook/chapter_1.html" target="_blank">NES Ebook</a>
    </Projeto>

    <Projeto 
        nome="Ray Tracing in One Weekend" 
        foto="https://raw.githubusercontent.com/Loukis-13/ray-tracing-in-one-weekend/master/images/image-21.png"
        repositorio="https://github.com/Loukis-13/ray-tracing-in-one-weekend"
        :linguagens="['Rust']"
    >
        Projeto para calcular a trajetória de raios de luz através de objetos.<br/>
        Desenvolvido com base no conteúdo do livro <a class="text-blue-500" href="https://raytracing.github.io/books/RayTracingInOneWeekend.html" target="_blank">Ray Tracing in One Weekend</a>
    </Projeto>

    <Projeto 
        nome="RSA® implementations" 
        foto="/projetos/rsa.png"
        repositorio="https://github.com/Loukis-13/RSA-implementations"
        :linguagens="['Python', 'Rust']"
    >
        Implementações do algoritmo RSA em diferentes linguagens utilizando diferentes bibliotecas, 
        com a implementação mais eficiente sendo em Python usando a biblioteca gmpy2, 
        conseguindo gerar chaves de 4096 em menos de 1 segundo e 10000 bits em 1 minuto e 50 segundos.
    </Projeto>

    <Projeto 
        nome="FOREX TRADING" 
        foto="/projetos/forex-trading/forex-trading.png"
        repositorio="https://github.com/Loukis-13/Forex-Trading"
        pagina="https://loukis-13.github.io/Forex-Trading/"
        :linguagens="['Javascript', 'Node', 'React', 'Nextjs', 'Tailwind']"
    >
        Aplicação checar a taxa de cambio entre multiplas moedas fácilmente.<br/>
        <br/>
        Dados monetários extraídos de <a class="text-blue-500" href="https://exchangerate.host/" target="_blank">exchangerate.host</a><br/>
    </Projeto>

    <Projeto 
        nome="InterFatecs" 
        foto="/projetos/InterFatecs.png"
        repositorio="https://github.com/Loukis-13/InterFatecs"
        :linguagens="['Python']"
    >
        Repositório de Problemas da Maratona de Programação <a class="text-blue-500" href="https://interfatecs.com.br/" target="_blank">InterFatecs</a>.
        <br/>
        No momento o repositório contém os problemas das maratonas de 2021 a 2023.
        <br/>
        <br/>
        Participei da maratona de 2022, ficando em 5° lugar e agora participo da maratona de 2023.
    </Projeto>

    <Projeto 
        nome="Demonstração de SQL"
        :linguagens="['PostgreSQL', 'SQLite']"
    >
        <template v-slot:imagem> 
            <div v-for="(v, i) in queries">
                <a v-show="i == query" class="text-3xl lg:text-4xl mb-2 text-blue-500 hover:underline" :href="v.link" target="_blank">{{ v.name }}</a>
                <pre v-show="i == query" class="w-full aspect-video"><code class="language-sql">{{ v.query }}</code></pre>
            </div>
        </template>

        Resoluções de desafios SQL do site CodeWars.
        A maioria das queries foram escritas para PostgreSQL, algumas para SQLite, 
        de acordo com as requisições dos desafios.
        <br />
        As queries demonstram diversos usos de funções do banco de dados e o link para
        a descrição do desafio se encontra no título da query.
        <br />
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
        Simples implementação da ferramenta Git em Ruby para apender os básicos da linguagem
    </Projeto>

    <Projeto 
        nome="DESAFIO FULLSTACK SIFAT" 
        foto="/projetos/desafio-sifat/demo.webp"
        repositorio="https://github.com/Loukis-13/desafio-fullstack-sifat"
        :linguagens="['Python', 'Javascript', 'Vue']"
    >
        Blog com sistema CRUD, composto por Django Framework no backend e VueJS no Frontend.<br/>
        <br/>
        O Blog possui um sistema de curtidas de cada post e criação/modificação/deleção de posts, sendo as duas funcionalidades feitas sem que haja atualização das páginas do sistema, por meio de chamadas assíncronas ao backend.
    </Projeto>

    <Projeto 
        nome="Musical" 
        foto="/projetos/musical/musical.png"
        repositorio="https://github.com/Loukis-13/musical-kotlin"
        :linguagens="['Java', 'Kotlin', 'Docker', 'Kafka']"
    >
        Micro-APIs para implementar um fluxo com banco de dados, OpenFeign para requesições en tre APIs, Kafka para mensageria e Docker Composer para orquestrar todos os serviços.<br/>
        <br/>
        <a class="text-blue-500" href="https://github.com/Loukis-13/musical">Versão em Java</a>
    </Projeto>

    <Projeto 
        nome="Currency API" 
        foto="/projetos/go-currency-api/go-currency-api.png"
        repositorio="https://github.com/Loukis-13/currency-API-GO"
        :linguagens="['GO', 'MongoDB']"
    >
        API para realizar trocas entre moedas<br/>
        <br/>
        Desenvolvida utilizando GOlang para back-end e MongoDB para banco de dados
    </Projeto>

    <Projeto 
        nome="DEMONSTAÇÕES DE ANÁLISES DE DADOS" 
        foto="/projetos/analise-de-dados/graficos.png"
        repositorio="https://github.com/Loukis-13/FCC_analise_de_dados" 
        :linguagens="['Python']"
    >
        Algoritimos de análise, manipulação, criação e transformação de dados, feitos em Python usando as bibliotecas
        Numpy, Pandas, Matplotlib e Seaborn.<br />
        <br />
        <div>
            <select v-model="dados" class="border border-gray-300 text-gray-900 block w-full p-2">
                <option :value="url_dados.mvs">Mean Variance Standard-deviation Calculator</option>
                <option :value="url_dados.medical_data">Medical Data Visualizer</option>
                <option :value="url_dados.demographic">Demographic Data Analyzer</option>
                <option :value="url_dados.page_view">Page View Time Series Visualizer</option>
                <option :value="url_dados.sea_level">Sea Level Predictor</option>
            </select>
            <br />
            <a class="bg-gray-600 p-2 rounded text-white" :href="dados" target="_blank">ABRIR</a>
        </div>
    </Projeto>

    <Projeto 
        nome="Back End Development and APIs" 
        foto="/projetos/FCC_APIs/fcc-apis.png"
        repositorio="https://github.com/Loukis-13/FCC_APIs"
        :linguagens="['Node']"
    >
        APIs desenvolvidas para a certificação do curso "APIs and Microservices" da Free Code Camp.<br/>
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

        O objetivo deste projeto é facilitar e agilizar a compra de produtos nas cantinas escolares para diminuir o tempo gasto em filas.<br/>
        Feito utilizando Django para o Back-end, Materialize css para o Front-end e mySQL para o banco de dados.
    </Projeto>

    <Projeto 
        nome="LEITOR ÁGIL" 
        foto="/projetos/leitor/leitor.png"
        repositorio="https://github.com/Loukis-13/leitor_agil"
        :linguagens="['Flutter', 'Dart']"
    >
        Aplicativo para mobiles para ajudar a ler arquivos e documentos rápidamente.<br/>
        Primeiramente feito utilizando Kivy para Python e depois atualizado para Flutter.<br/>
        <br/>
        <a class="text-blue-500" href="https://github.com/Loukis-13/Leitor-agil" target="_blank">Versão em Python</a>
    </Projeto>

    <Projeto 
        nome="GESSO MORRO AGUDO" 
        foto="/projetos/gesso/gesso.png"
        repositorio="https://github.com/Loukis-13/gesso-morro-agudo"
        pagina="https://loukis-13.github.io/gesso-morro-agudo/"
        :linguagens="['Python', 'Javascript']"
    >
        Catálogo simples que extrai os dados de um csv<br/>
    </Projeto>

    <Projeto 
        nome="FRASES CÔMICAS DOS PRESIDENTES" 
        foto="/projetos/frases-comicas-dos-presidentes/frases-comicas-dos-presidentes.png"
        repositorio="https://github.com/Loukis-13/frases_presidentes"
        pagina="https://loukis-13.github.io/frases_presidentes/"
        :linguagens="['Python']"
    >
        Microserviço para servir as frases mais cômicas dos presidentes do Brasil<br/>
        Feito utilizando Flask para Python<br/>
    </Projeto>
</template>