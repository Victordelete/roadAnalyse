<template>
  <PageCabecalho />

  <div class="bar">
    <button class="bar-item item-button" @click=" openCity('Login')">Login</button>
    <button class="bar-item item-button" @click="openCity('Enviar_Arquivo')">Enviar Arquivo</button>
    <button class="bar-item item-button" @click=" openCity('Info_Rodovia')">Info. Rodovia</button>
  </div>

  <div id="Login" class="city" style="display:none">
    <PageLogin />
  </div>

  <div id="Enviar_Arquivo" class="city">
    <PageEnviaArquivo />
  </div>

  <div id="Info_Rodovia" class="city" style="display:none">
    <PageInforodo />
  </div>
  
</template>

<script>
import PageEnviaArquivo from './components/PageEnviaArquivo.vue'
import PageCabecalho from './components/PageCabecalho.vue'
import PageInforodo from './components/PageInforodo.vue'
import PageLogin from './components/PageLogin.vue'

export default {
  name: 'App',
  components: {
    PageEnviaArquivo,
    PageCabecalho,
    PageInforodo,
    PageLogin
},
  methods:{ 
    openCity(cityName) {
      var i;
      var x = document.getElementsByClassName("city");
      for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";  
      }
      document.getElementById(cityName).style.display = "block";  
    }
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

.bar{
  display: flex;
}
.bar-item{

}
.item-button{

}
</style>
