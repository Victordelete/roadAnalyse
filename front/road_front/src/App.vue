<template>
  <PageCabecalho />
  <PageEnviaArquivo />
  <PageInforodo />
  <PageInfoAvg />
</template>

<script>
import PageEnviaArquivo from './components/PageEnviaArquivo.vue'
import PageCabecalho from './components/PageCabecalho.vue'
import PageInforodo from './components/PageInforodo.vue'

export default {
  name: 'App',
  components: {
    PageEnviaArquivo,
    PageCabecalho, 
    PageInforodo
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
