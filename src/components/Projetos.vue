<script setup>
const lista_projetos = [
    {
        nome: 'DUNGEON RAIDERS',
        descrição: `\
            Jogo digital criado com base no jogo de cartas <a href="https://www.ludopedia.com.br/jogo/dungeon-raiders" target="_blank">Dungeon Raiders</a>.
            Inicialmente feito utilizando Kivy para Python e depois mudado para Phaser 3.
            Versão para um jogador terminada, versão para dois jogadores em desenvolvimento.

            <a href="https://loukis-13.github.io/Dungeon-Raiders-Phaser/" target="_blank">JOGAR</a>

            <a href="https://github.com/Loukis-13/Dungeon-Raiders-Phaser" target="_blank">CÓDIGO NO GITHUB</a>
        `,
        foto: 'img/dungeon/tela1.png',
        linguagens: [
            'Javascript'
        ]
    },
    {
        nome: 'ESTE SITE',
        descrição: `\
            Feitocom Vue 3 utilizando Composition API e Vite

            <a href="https://github.com/Loukis-13/Loukis-13.github.io" target="_blank">CÓDIGO NO GITHUB</a>
        `,
        foto: 'img/portifolio/portifolio.png',
        linguagens: [
            'Javascript',
            'Vue'
        ]
    },
    {
        nome: 'DESAFIO FULLSTACK SIFAT',
        descrição: `\
            Blog com sistema CRUD, composto por Django Framework no backend e VueJS no Frontend.

            O Blog possui um sistema de curtidas de cada post e criação/modificação/deleção de posts, sendo as duas funcionalidades feitas sem que haja atualização das páginas do sistema, por meio de chamadas assíncronas ao backend.

            <a href="https://github.com/Loukis-13/desafio-fullstack-sifat" target="_blank">CÓDIGO NO GITHUB</a>
        `,
        foto: 'img/desafio-sifat/demo.gif',
        linguagens: [
            'Python',
            'Javascript',
            'Vue'
        ]
    },
    {
        nome: 'Musical',
        descrição: `
            Micro-APIs para implementar um fluxo com banco de dados, OpenFeign para requesições en tre APIs, Kafka para mensageria e Docker Composer para orquestrar todos os serviços.

            <a href="https://github.com/Loukis-13/musical">CÓDIGO NO GITHUB (Java)</a>
            <a href="https://github.com/Loukis-13/musical-kotlin">CÓDIGO NO GITHUB (Kotlin)</a>
        `,
        foto: 'img/musical/musical.png',
        linguagens: [
            'Java',
            'Kotlin',
            'Docker',
            'Kafka'
        ]
    },
    {
        nome: 'Currency API',
        descrição: `\
            API para realizar trocas entre moedas

            Desenvolvida utilizando GOlang para back-end e MongoDB para banco de dados
            
            <a href="https://github.com/Loukis-13/currency-API-GO" target="_blank">CÓDIGO NO GITHUB</a>
        `,
        foto: 'img/go-currency-api/go-currency-api.png',
        linguagens: [
            'GO',
            'MongoDB'
        ]
    },
    {
        nome: 'Back End Development and APIs',
        descrição: `\
            APIs desenvolvidas para a certificação do curso "APIs and Microservices" da Free Code Camp.
            Escritas Node.js e implementadas na plataforma do Heroku, todas as APIs foram reunidas em um único app para melhor manueseio.

            <a href="https://github.com/Loukis-13/FCC_APIs" target="_blank">CÓDIGO NO GITHUB</a>
        `,
        foto: 'img/FCC_APIs/fcc-apis.png',
        linguagens: [
            'Node'
        ]
    },
    {
        nome: 'DEMONSTAÇÕES DE ANÁLISES DE DADOS',
        descrição: `\
            Algoritimos de análise, manipulação, criação e transformação de dados, feitos em Python usando as bibliotecas Numpy, Pandas, Matplotlib e Seaborn

            <div>
                <select id="opcaoAnaliseDeDados" class="browser-default">
                    <option value="mvs" selected>Mean Variance Standard-deviation Calculator</option>
                    <option value="medical_data">Medical Data Visualizer</option>
                    <option value="demographic">Demographic Data Analyzer</option>
                    <option value="page_view">Page View Time Series Visualizer</option>
                    <option value="sea_level">Sea Level Predictor</option>
                </select>
                <button class="btn" onclick="open_dados()">ABRIR</button>
            </div>
            <a href="https://github.com/Loukis-13/FCC_analise_de_dados" target="_blank">CÓDIGO NO GITHUB</a>
        `,
        foto: 'img/analise-de-dados/graficos.png',
        linguagens: [
            'Python'
        ]
    },
    {
        nome: 'NOSSA CANTINA',
        descrição: `\
            O objetivo deste projeto é facilitar e agilizar a compra de produtos nas cantinas escolares para diminuir o tempo gasto em filas.
            Feito utilizando Django para o Back-end, Materialize css para o Front-end e mySQL para o banco de dados.

            <a href="https://github.com/Loukis-13/nossa-cantina" target="_blank">CÓDIGO NO GITHUB</a>
        `,
        foto: 'img/nossa-cantina/1.png',
        linguagens: [
            'Python',
            'Javascript',
            'MySQL'
        ]
    },
    {
        nome: 'LEITOR ÁGIL',
        descrição: `\
            Aplicativo para mobiles para ajudar a ler arquivos e documentos rápidamente.
            Primeiramente feito utilizando Kivy para Python e depois atualizado para Flutter.
            
            <a href="https://github.com/Loukis-13/leitor_agil" target="_blank">CÓDIGO NO GITHUB (Dart)</a>
            <a href="https://github.com/Loukis-13/Leitor-agil" target="_blank">CÓDIGO NO GITHUB (Python)</a>
        `,
        foto: 'img/leitor/leitor.png',
        linguagens: [
            'Flutter',
            'Dart'
        ]
    },
    {
        nome: 'GESSO MORRO AGUDO',
        descrição: `\
            Catálogo simples que extrai os dados de um csv

            <a href="https://github.com/Loukis-13/gesso-morro-agudo" target="_blank">CÓDIGO NO GITHUB</a>
            
            <a href="https://loukis-13.github.io/gesso-morro-agudo/" target="_blank">GIT PAGE</a>
        `,
        foto: 'img/gesso/gesso.png',
        linguagens: [
            'Python',
            'Javascript'
        ]
    },
    {
        nome: 'FRASES CÔMICAS DOS PRESIDENTES',
        descrição: `\
            Microserviço para servir as frases mais cômicas dos presidentes do Brasil
            Feito utilizando Flask para Python

            <a href="https://github.com/Loukis-13/frases_presidentes" target="_blank">CÓDIGO NO GITHUB</a>

            <a href="https://loukis-13.github.io/frases_presidentes/" target="_blank">GIT PAGE</a>
        `,
        foto: 'img/frases-comicas-dos-presidentes/frases-comicas-dos-presidentes.png',
        linguagens: [
            'Python'
        ]
    },
]

const url_dados = {
    mvs: 'https://colab.research.google.com/drive/1XqWO1akL_v2Rvve8x1E-qQqvRqnI3kxy?usp=sharing',
    medical_data: 'https://colab.research.google.com/drive/1gabe6Tdy0SfPBIpHG1_FJ0168imXz7h1?usp=sharing',
    demographic: 'https://colab.research.google.com/drive/1z-AFWAm185-hAy_kAYYNYAuRvFu-9cE_?usp=sharing',
    page_view: 'https://colab.research.google.com/drive/11qkOfJlo-8JKne7wPtd39xVINqLYS-vJ?usp=sharing',
    sea_level: 'https://colab.research.google.com/drive/17_eYVYndSfQ5lVeltbytLF2NbBtMluyM?usp=sharing'
}

function open_dados() {
    window.open(url_dados[document.getElementById("opcaoAnaliseDeDados").value])
}
</script>

<template>
    <div v-for="(p, i) in lista_projetos" :class="`col grey darken-${i%2+2}`" style="padding-top: 2% !important;width: 100%">
        <div class="col l6 m12">
            <div class="row">
                <div class="col l1 m12 s12">
                    <div class="row">
                        <img v-for="x in p.linguagens" class="responsive-img col l12 s2" :src="`img/logos/${x}.svg`" :alt="x" :title="x" style="padding: .5rem;">
                    </div>
                </div>
                <img class="col l11 m12 s12" :src="p.foto">
            </div>
        </div>
        <div class="col l6 m12 s12">
            <h2 style="margin: 0;">{{p.nome}}</h2>
            <h5 v-html="p.descrição"></h5>
        </div>
    </div>
</template>