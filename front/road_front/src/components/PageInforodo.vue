<template>
    <div class="enviarRequest">
        <h1>
            Solicita informação.
        </h1>

        <p>
            Solicitar km com maior incidência. [Buraco, Remendo, Trinca]
        </p>

        <div class="item">
            <label for="rodovia">Rodovia</label>
            <input type="text" name="rodovia" multiple ref="rodovia" id="rodovia" />
        </div>

        <div class="item">
            <label for="coluna">Item</label>
            <input type="text" name="coluna" multiple ref="coluna" id="coluna" />
        </div>

        <div class="item">
            <button @click="sendRequest">Enviar</button>
        </div>

        <div class="item">
            <label for="resposta">Resposta</label>
            <textarea rows="1" disabled="True" type="text" name="resposta" multiple ref="resposta" id="resposta" />
        </div>

    </div>

    <hr>
</template>

<script>
export default {
    name: 'App',
    methods: {
        async sendRequest() {
            let rodovia = document.getElementById("rodovia").value
            var coluna = document.getElementById("coluna").value

            var jsonString = {
                rodovia: rodovia,
                item: coluna
            };

            var jsonData = JSON.stringify(jsonString)
            console.log(jsonData) 

            fetch('http://localhost:5000/rodovia', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json' 
                },
                body: jsonData
            })
                .then(response => response.json()) 
                .then(data => {
                    console.log('Resposta da API:', data);
                    document.getElementById("resposta").value = data + ' km';

                })
                .catch(error => {
                    console.error('Erro ao fazer a requisição:', error);
                });
        },
    },
};

</script>

<style>
.enviarRequest {
    margin: 1px;
    padding: 0 1rem;

    display: inline;
    align-items: center;
    justify-content: center;
}

.item {
    padding-top: 1%;
    padding-bottom: 1%;
}

label {
    display: block;
}
</style>
