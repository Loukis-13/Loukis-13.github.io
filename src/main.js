import { createApp } from 'vue'
import { createI18n } from "vue-i18n"
import App from './App.vue'
import pt from "./locales/pt.js"
import en from "./locales/en.js"

import './index.css'
import '@splidejs/vue-splide/css';

import 'prismjs'
import 'prismjs/components/prism-sql';
import 'prism-themes/themes/prism-vsc-dark-plus.css';


const i18n = createI18n({
    locale: "en",
    legacy: false,
    messages: {
        pt,
        en
    }
})

const usersLanguage = window.navigator.language.split("-")[0]
const availibleLocales = i18n.global.availableLocales;

if (availibleLocales.includes(usersLanguage)) {
    i18n.global.locale.value = usersLanguage;
}

createApp(App)
    .use(i18n)
    .mount('#app')
