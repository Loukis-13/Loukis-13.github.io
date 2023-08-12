<script setup>
defineProps(['nome', 'linguagens', 'foto', 'repositorio', 'pagina'])
</script>

<template>
    <div :id="nome" class="grid lg:grid-cols-2 gap-5 px-2 pb-2 w-full bg-neutral-800 even:bg-neutral-600 odd:text-neutral-400 even:text-neutral-950">
        <div class="grid lg:grid-cols-12 mt-2 lg:my-5  overflow-auto">
            <div class="pe-1 grid grid-cols-10 lg:grid-cols-1 auto-rows-min flex items-center">
                <img v-for="x in linguagens" class="p-1 pb-2 w-96" :src="`/logos/${x}.svg`" :alt="x" :title="x" />
            </div>
            <div class="col-span-11 overflow-auto">
                <slot name="imagem">
                    <img class="w-full aspect-video" :src="foto" />
                </slot>
            </div>
        </div>
        <div>
            <div class="grid grid-cols-12 lg:my-5">
                <div>
                    <a v-if="pagina" :href="pagina" target="_blank">
                        <img class="bg-blend-white" src="@/assets/redirect.svg" title="Visitar página" />
                    </a>
                </div>
                <h2 class="text-3xl lg:text-4xl mb-2 col-span-10">{{ nome }}</h2>
                <a :href="repositorio" target="_blank">
                    <img v-if="repositorio" src="/redes-sociais/github.svg" title="Código no GitHub" />
                </a>
            </div>
            <div class="text-xl">
                <slot></slot>
            </div>
        </div>
    </div>
</template>