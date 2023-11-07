# ROADANALYSE

Projeto apresenta interface web composta por API (Flask) e página frontend (VueJs) para gestão das informçaões. Dados armazenados em banco de dados Postgres, iniciando automáticamente via Script.

## REQUISITOS

### ENTREGUES

- Utilizar Python com Peewee - Valor: 1,5pts ;
- Utilizar Sqlite - Valor: 1,5pts ;
- Criar tabela results no banco de dados - Valor: 1,0pt ;
- Exportar resultados em um csv agrupados corretamente - Valor: 1,0 pt.
- Utilizar Postgres + PostGIS - Valor: 2,0pt; (Substitui o sqlite ).
- Criar uma API com Tornado, Flask, Django ou similar (Neste caso, tira a obrigatoriedade da utilização do Peewee ) - Valor: 2,0pt ;
- Criar scripts de criação automática das tabelas (init.sql) - Valor: 0.5pt;
- Permitir consulta do tipo qual Km de determinada rodovia possui maior incidência de determinado item - Valor: 1.0pt;
- Criar tabelas do tipo View para auxiliar em querys - Valor: 0.5pt;
- Criar tabelas auxiliares no banco de dados:
    1. Criar tabela vídeos com km Ini e Km Final de cada vídeo no banco de dados - Valor: 0.5pt;
    2. Criar tabela rodovias com km Ini e Km Final (de acordo com os km que foram levantados) de cada rodovia no banco de dados - Valor: 0.5pt;
- Utilizar Docker - Valor: 1.0pt;
- Criar interface gráfica com vueJs - Valor: 1.0pt;
- Utilizar ElectronJs- Valor: 1.0pt;

### NÃO ENTREGUES

- Utilize OpenLayers ou Leaflet para mostrar os dados levantados em um mapa - Valor: 1.0pt
- Criar função para calcular o KM de determinado item - Valor: 1.0pt; para isso utilize a ‘ latitude’ e ‘ longitude’ e a camada do SNV202304A (a qual possui os traçados e quilômetros de referências de rodovias federais do Brasil), use a coluna ‘exp_km_calc’ (valor inteiro do km calculado) como referência para validar seus resultados. ( Dica: Utilize shapely.geometry.LineString( ).project(point,normalized=True) )

## COMANDOS

npm run serve
npm run electron:serve

## UTILIZAÇÃO 

Pasta para os arquivos de saída com o nome da rodovia, com sobreposição. 

### ROTAS APIs
- /info
    1. Apresenta página estática com informações do desenvolvedor. 
- /data
    1. Recebe arquivo com Key: 'file' e arquivo csv de dados. 
    2. Retorna True/False se Sucesso/Erro. 
- /rodovia
    1. Recebe Json com "rodovia" e "item" em string. 
    2. Retorna lista com kms com maior indicência do "item" na "rodovia". 
- /above_avg
    1. Recebe Json com "tabela endereçando item (Buraco, Trinca ou Remendo). 
    2. Retorna lista com rodovias, kms e incidência do "item" acima da média. 


## VERSÕES

Python 3.12.0
Flask 3.0.0
Werkzeug 3.0.1
numpy 1.26.1
pandas 2.1.1
psycopg2 2.9.9
SQLAlchemy 2.0.22

## RUN DOCKER

docker image build -t road_api_docker .
docker run -p 5000:5000 -d road_api_docker