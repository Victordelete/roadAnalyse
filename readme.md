## REQUISITOS

### ENTREGUES

- Utilizar Python com Peewee - Valor: 1,5pts ;
- Utilizar Sqlite - Valor: 1,5pts ;
- Criar tabela results no banco de dados - Valor: 1,0pt ;
- Exportar resultados em um csv agrupados corretamente - Valor: 1,0 pt.
- Utilizar Postgres + PostGIS - Valor: 2,0pt; (Substitui o sqlite ).
- Criar uma API com Tornado, Django ou similar (Neste caso, tira a obrigatoriedade da utilização do Peewee ) - Valor: 2,0pt ;
- Criar scripts de criação automática das tabelas (init.sql) - Valor: 0.5pt;
- Permitir consulta do tipo qual Km de determinada rodovia possui maior incidência de determinado item - Valor: 1.0pt;
- Criar tabelas do tipo View para auxiliar em querys - Valor: 0.5pt;
- Criar tabelas auxiliares no banco de dados:
    1. Criar tabela vídeos com km Ini e Km Final de cada vídeo no banco de dados - Valor: 0.5pt;
- Utilizar Docker - Valor: 1.0pt;
- Criar interface gráfica com vueJs - Valor: 1.0pt;

### NÃO ENTREGUES

- Utilizar ElectronJs- Valor: 1.0pt;
- Utilize OpenLayers ou Leaflet para mostrar os dados levantados em um mapa - Valor: 1.0pt
- Criar função para calcular o KM de determinado item - Valor: 1.0pt; para isso utilize a ‘ latitude’ e ‘ longitude’ e a camada do SNV202304A (a qual possui os traçados e quilômetros de referências de rodovias federais do Brasil), use a coluna ‘exp_km_calc’ (valor inteiro do km calculado) como referência para validar seus resultados. ( Dica: Utilize shapely.geometry.LineString( ).project(point,normalized=True) )

## COMANDOS

npm run serve
npm run electron:serve

## UTILIZAÇÃO 

pasta para os arquivos de saída com o nome da rodovia, com sobreposição. 

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