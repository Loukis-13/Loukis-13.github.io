<script setup>
const lista_certificacoes = [
    {
        nome: 'PCAP – Certified Associate in Python Programming',
        url: 'https://www.credly.com/badges/a2686b60-1493-41af-965c-5e9e08909347/public_url'
    },
    {
        nome: 'Certified Entry-Level JavaScript Programmer',
        url: 'https://www.credly.com/badges/57d503c0-2760-4833-8653-a7f6b052c4df/public_url'
    },
    {
        nome: 'English Proficiency C1',
        url: 'https://www.credly.com/badges/31d824ed-1614-40af-9390-bd591e675392/public_url'
    },
    {
        nome: 'CCNA: Introduction to Networks',
        url: 'https://www.credly.com/badges/bc0bb1e5-b019-4aa5-b0c8-27e298873dac/public_url'
    },
    {
        nome: 'CCNA: Switching, Routing, and Wireless Essentials',
        url: 'https://www.credly.com/badges/9c7b0438-aac9-4461-8ff8-15f6874cd5b3/public_url'
    },
    {
        nome: '4YOU2 Certificate',
        url: 'https://www.credly.com/badges/31d824ed-1614-40af-9390-bd591e675392/public_url'
    },
    {
        nome: 'JavaScript Algorithms and Data Structures',
        url: 'https://www.freecodecamp.org/certification/loukis/javascript-algorithms-and-data-structures'
    },
    {
        nome: 'Back End Development and APIs',
        url: 'https://www.freecodecamp.org/certification/loukis/back-end-development-and-apis'
    },
    {
        nome: 'Scientific Computing with Python',
        url: 'https://www.freecodecamp.org/certification/loukis/scientific-computing-with-python-v7'
    },
    {
        nome: 'Data Analysis with Python',
        url: 'https://www.freecodecamp.org/certification/loukis/data-analysis-with-python-v7'
    },
    {
        nome: 'Python 3 CG',
        url: 'https://www.codingame.com/certification/bIiH1wbTcBe59jliDfnkEA'
    },
    {
        nome: 'JavaScript CG',
        url: 'https://www.codingame.com/certification/E_wWSv4rLAT_KmRUBkp_kw'
    },
    {
        nome: 'Rust CG',
        url: 'https://www.codingame.com/certification/lL7ufXJbX-Hpej5hmXB8Rg'
    },
    {
        nome: 'Java CG',
        url: 'https://www.codingame.com/certification/Nqr7oPdhLmFhY4TsXnGnyw'
    },
    {
        nome: 'Coding Speed',
        url: 'https://www.codingame.com/certification/YiWruQpxHnd4p3Uvh3HNMg'
    },
    {
        nome: 'Algorithms',
        url: 'https://www.codingame.com/certification/YYdpk3fEJNVyNlg09LwVgg'
    },
    {
        nome: 'Colaboration',
        url: 'https://www.codingame.com/certification/2UvC_t5Nq5IGgiR9QtGchg'
    },
    {
        nome: 'Extreme Go Horse',
        url: 'https://www.gohorsecertification.com.br/'
    },
]
</script>

<template>
    <a v-for="c in lista_certificacoes" class="col xl2 l3 s6" :href="c.url" target="_blank">
        <img class="responsive-img" :src="`img/certificações/${c.nome}.png`" :alt="c.nome" :title="c.nome" style="padding: 4%;">
    </a>
</template>