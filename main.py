diagrama_html = """\
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Loukis</title>
    <link rel="shortcut icon" href="img/redes-sociais/git.png">
    <link rel="stylesheet" href="materialize/materialize.min.css">
    <link rel="stylesheet" href="splide/splide.min.css">
    <link rel="stylesheet" href="index.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>

<body class="grey lighten-2">
    <div class="black" style="padding-bottom: 1% !important;">
        <div class="row valign-wrapper">
            <div class="col l4 m8">
                <div class="row grey" style="border-bottom-right-radius: 3vw;">
                    <a class="col s2 m-1" href="https://github.com/Loukis-13" target="_blank"><img class="responsive-img" src="img/redes-sociais/git.png"></a>
                    <a class="col s2 m-1" href="https://www.linkedin.com/in/jose-nivaldo-da-silva-hypolito/" target="_blank"><img class="responsive-img" src="img/redes-sociais/linkedin.png" style="border-radius: 10%;"></a>
                    <a class="col s2 m-1" href="https://replit.com/repls" target="_blank"><img class="responsive-img" src="img/redes-sociais/replit.png"></a>
                    <a class="col s2 m-1" href="https://web.digitalinnovation.one/users/ze_zinho-2010?tab=achievements" target="_blank"><img class="responsive-img" src="img/redes-sociais/dio.png" style="background-color: transparent;"></a>
                    <a class="col s2 m-1" href="https://www.freecodecamp.org/loukis" target="_blank"><img class="responsive-img" src="img/redes-sociais/fcc.png"></a>
                </div>
            </div>
            <a class="col l8 m4 hide-on-med-and-down" href="https://www.codewars.com/users/Loukis" target="_blank"><img class="right" src="https://www.codewars.com/users/Loukis/badges/large"></a>
            <a class="col l8 m4 hide-on-large-only" href="https://www.codewars.com/users/Loukis" target="_blank"><img class="right" src="https://www.codewars.com/users/Loukis/badges/micro"></a>
        </div>

        <h1 class="white-text" style="margin-top: 0;">JOSÉ NIVALDO DA SILVA HYPÓLITO</h1>
        <h2 class="white-text">DESENVOLVEDOR</h2>
        <div class="langs splide" role="group" style="margin: 0 5%;">
            <div class="splide__track">
                <div class="row splide__list" style="display: flex;align-items: center;">
                    {}
                </div>
            </div>
        </div>
    </div>

    <div class="row" style="margin-bottom: 0;">
        {}

        <div class="col s12 grey darken-4" style="padding-bottom: 3%;">
            <h2 class="white-text" style="margin: 3% 0;">CERTIFICAÇÕES</h2>
            {}
        </div>
    </div>

    <script src="splide/splide.min.js"></script>
    <script src="splide/splide-extension-auto-scroll.min.js"></script>
    <script>
        url_dados = {{
            'mvs': 'https://colab.research.google.com/drive/1XqWO1akL_v2Rvve8x1E-qQqvRqnI3kxy?usp=sharing',
            'medical_data': 'https://colab.research.google.com/drive/1gabe6Tdy0SfPBIpHG1_FJ0168imXz7h1?usp=sharing',
            'demographic': 'https://colab.research.google.com/drive/1z-AFWAm185-hAy_kAYYNYAuRvFu-9cE_?usp=sharing',
            'page_view': 'https://colab.research.google.com/drive/11qkOfJlo-8JKne7wPtd39xVINqLYS-vJ?usp=sharing',
            'sea_level': 'https://colab.research.google.com/drive/17_eYVYndSfQ5lVeltbytLF2NbBtMluyM?usp=sharing'
        }}

        function open_dados() {{
            window.open(url_dados[document.getElementById("opcaoAnaliseDeDados").value])
        }}

        new Splide('.splide', {{
            type: 'loop',
            drag: 'free',
            perPage: 10,
            arrows: false,
            pagination: false,
            breakpoints: {{
                640: {{
                    perPage: 4,
                }},
            }},
            autoScroll: {{
                speed: 1,
            }},
        }}).mount(window.splide.Extensions);
    </script>
</body>

</html>\
"""

diagrama_linugagem_header = '<img class="col l1 s2 splide__slide" style="margin: 0;" src="img/logos/{0}.svg" alt="{1}" title="{1}">'

diagrama_projeto = """
        <div class="col grey darken-{cor}" style="padding-top: 2% !important;width: 100%">
            <div class="col l6 m12">
                <div class="row">
                    <div class="col l1 m12 s12">
                        <div class="row">
                            {linguagens}
                        </div>
                    </div>
                    <img class="col l11 m12 s12" src="{foto}">
                </div>
            </div>
            <div class="col l6 m12 s12">
                <h2 style="margin: 0;">{nome}</h2>
                <h5>{descrição}</h5>
            </div>
        </div>
"""

diagrama_projeto_linguagem = '<img class="responsive-img col l12 s2" src="img/logos/{0}.svg" alt="{0}" title="{0}" style="padding: .5rem;">'

diagrama_certificacoes = """\
    <a class="col xl2 l3 s6" href="{url}" target="_blank">
        <img class="responsive-img" src="img/certificações/{nome}.png" alt="{nome}" title="{nome}" style="padding: 4%;">
    </a>\
"""



lista_linguagens = ["C#", "Java", "Kotlin", "Rust", "Python", "Javascript", "GO",  "Lua", "C", "C++"]

lista_projetos = [
    {
        'nome': 'DUNGEON RAIDERS',
        'descrição': '''\
            Jogo digital criado com base no jogo de cartas <a href="https://www.ludopedia.com.br/jogo/dungeon-raiders" target="_blank">Dungeon Raiders</a>.
            Inicialmente feito utilizando Kivy para Python e depois mudado para Phaser 3.
            Versão para um jogador terminada, versão para dois jogadores em desenvolvimento.

            <a href="https://loukis-13.github.io/Dungeon-Raiders-Phaser/" target="_blank">JOGAR</a>

            <a href="https://github.com/Loukis-13/Dungeon-Raiders-Phaser" target="_blank">CÓDIGO NO GITHUB</a>
        ''',
        'foto': 'img/dungeon/tela1.png',
        'linguagens': [
            'Javascript'
        ]
    },
    {
        'nome': 'Back End Development and APIs',
        'descrição': '''\
            APIs desenvolvidas para a certificação do curso "APIs and Microservices" da Free Code Camp.
            Escritas Node.js e implementadas na plataforma do Heroku, todas as APIs foram reunidas em um único app para melhor manueseio.

            <a href="https://github.com/Loukis-13/FCC_APIs" target="_blank">CÓDIGO NO GITHUB</a>
        ''',
        'foto': 'img/FCC_APIs/fcc-apis.png',
        'linguagens': [
            'Node'
        ]
    },
    {
        'nome': 'DEMONSTAÇÕES DE ANÁLISES DE DADOS',
        'descrição': '''\
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
        ''',
        'foto': 'img/analise-de-dados/graficos.png',
        'linguagens': [
            'Python'
        ]
    },
    {
        'nome': 'LEITOR ÁGIL',
        'descrição': '''\
            Aplicativo para mobiles para ajudar a ler arquivos e documentos rápidamente.
            Feito utilizando Kivy para Python.

            <a href="https://mega.nz/file/TzpCmAjD#LFH9cb6-01HEWKOTLQWG39lfwAG61NdIpOUMEsWETmc" target="_blank">ANDROID</a>

            <a href="https://github.com/Loukis-13/Leitor-agil" target="_blank">CÓDIGO NO GITHUB</a>
        ''',
        'foto': 'img/leitor/leitor.png',
        'linguagens': [
            'Python'
        ]
    },
    {
        'nome': 'NOSSA CANTINA',
        'descrição': '''\
            O objetivo deste projeto é facilitar e agilizar a compra de produtos nas cantinas escolares para diminuir o tempo gasto em filas.
            Feito utilizando Django para o Back-end, Materialize css para o Front-end e mySQL para o banco de dados.

            <a href="https://github.com/Loukis-13/nossa-cantina" target="_blank">CÓDIGO NO GITHUB</a>
        ''',
        'foto': 'img/nossa-cantina/1.png',
        'linguagens': [
            'Python',
            'Javascript',
            'MySQL'
        ]
    },
    {
        'nome': 'GESSO MORRO AGUDO',
        'descrição': '''\
            Catálogo simples que extrai os dados de um csv

            <a href="https://github.com/Loukis-13/gesso-morro-agudo" target="_blank">CÓDIGO NO GITHUB</a>
            <a href="https://loukis-13.github.io/gesso-morro-agudo/" target="_blank">GIT PAGE</a>
        ''',
        'foto': 'img/gesso/gesso.png',
        'linguagens': [
            'Python',
            'Javascript'
        ]
    },
    {
        'nome': 'FRASES CÔMICAS DOS PRESIDENTES',
        'descrição': '''\
            Microserviço para servir as frases mais cômicas dos presidentes do Brasil
            Feito utilizando Flask para Python

            <a href="https://github.com/Loukis-13/frases_presidentes" target="_blank">CÓDIGO NO GITHUB</a>
        ''',
        'foto': 'img/frases-comicas-dos-presidentes/frases-comicas-dos-presidentes.png',
        'linguagens': [
            'Python'
        ]
    },
    {
        'nome': 'Currency API',
        'descrição': '''\
            API para realizar trocas entre moedas

            Desenvolvida utilizando GOlang para back-end e MongoDB para banco de dados
            
            <a href="https://github.com/Loukis-13/currency-API-GO" target="_blank">CÓDIGO NO GITHUB</a>
        ''',
        'foto': 'img/go-currency-api/go-currency-api.png',
        'linguagens': [
            'GO',
            'MongoDB'
        ]
    },
    {
        'nome': 'Musical',
        'descrição': '''
            Micro-APIs para implementar um fluxo com banco de dados, OpenFeign para requesições en tre APIs, Kafka para mensageria e Docker Composer para orquestrar todos os serviços.

            <a href="https://github.com/Loukis-13/musical">CÓDIGO NO GITHUB (Java)</a>
            <a href="https://github.com/Loukis-13/musical-kotlin">CÓDIGO NO GITHUB (Kotlin)</a>
        ''',
        'foto': 'img/musical/musical.png',
        'linguagens': [
            'Java',
            'Kotlin',
            'Docker',
            'Kafka'
        ]
    },
    # {
    #     'nome': '',
    #     'descrição': '''
            
    #     ''',
    #     'foto': '',
    #     'linguagens': [
    #         ''
    #     ]
    # },
]

lista_certificacoes = [
    {
        'nome': 'PCAP – Certified Associate in Python Programming',
        'url': 'https://www.credly.com/badges/a2686b60-1493-41af-965c-5e9e08909347/public_url'
    },
    {
        'nome': 'Certified Entry-Level JavaScript Programmer',
        'url': 'https://www.credly.com/badges/57d503c0-2760-4833-8653-a7f6b052c4df/public_url'
    },
    {
        'nome': 'CCNA: Introduction to Networks',
        'url': 'https://www.credly.com/badges/bc0bb1e5-b019-4aa5-b0c8-27e298873dac/public_url'
    },
    {
        'nome': 'CCNA: Switching, Routing, and Wireless Essentials',
        'url': 'https://www.credly.com/badges/9c7b0438-aac9-4461-8ff8-15f6874cd5b3/public_url'
    },
    {
        'nome': 'JavaScript Algorithms and Data Structures',
        'url': 'https://www.freecodecamp.org/certification/loukis/javascript-algorithms-and-data-structures'
    },
    {
        'nome': 'Back End Development and APIs',
        'url': 'https://www.freecodecamp.org/certification/loukis/back-end-development-and-apis'
    },
    {
        'nome': 'Scientific Computing with Python',
        'url': 'https://www.freecodecamp.org/certification/loukis/scientific-computing-with-python-v7'
    },
    {
        'nome': 'Data Analysis with Python',
        'url': 'https://www.freecodecamp.org/certification/loukis/data-analysis-with-python-v7'
    },
]



open('index.html', 'w').write(diagrama_html.format(
    "\n".join(diagrama_linugagem_header.format(i if i != 'C#' else 'CS', i) for i in lista_linguagens),
    "\n".join(diagrama_projeto.format(**{**p, 'cor': 2+i%2, 'linguagens': '\n'.join(diagrama_projeto_linguagem.format(j) for j in p['linguagens'])}) for i, p in enumerate(lista_projetos)),
    "\n".join(diagrama_certificacoes.format(**c) for c in lista_certificacoes)
))
