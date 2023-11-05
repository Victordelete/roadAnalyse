<template>
  <div class="enviaArquivo item">
    <h1 class="item">
      Enviar arquivo.
    </h1>

    <p>
      Envia arquivo com informações coletadas das rodovidas. 
    </p>

    <div class="item">
      <input type="file" name="file" multiple ref="files"  />
    </div>

    <div class="item">
      <button @click="sendFile">Enviar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    async sendFile() {
      let dataForm = new FormData();
      for (let file of this.$refs.files.files) {
        dataForm.append(`file`, file);
      }
      let res = await fetch(`http://localhost:5000/data`, {
        method: 'POST',
        body: dataForm,
      });
      let data = await res.json();
      console.log(data);
    },
  },
};
</script>

<style>
.enviaArquivo {
  margin: 1px;
  padding-top: 1px;
  padding-top: 5px;

  display: inline;
  align-items: center;
  justify-content: center;
}

.item {
    padding-top: 1%;
    padding-bottom: 1%;
}

</style>
