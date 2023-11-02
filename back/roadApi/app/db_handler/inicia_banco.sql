/*
Arquivo cria em SQL a tabela de resultado proposta para o desafio.
Arquivo idealizado como um script que inicia a tabela de resultados. 
*/

CREATE TABLE IF NOT EXISTS  RESULTS(
    "highway" VARCHAR(100),
    "exp_km_calc" DOUBLE PRECISION,
    "Buraco" INT,
    "Drenagem" INT,
    "Faixa Central" INT,
    "Faixa Lateral" INT,
    "Placa" INT,
    "Remendo" INT,
    "Rocada" INT,
    "Trinca" INT
);

CREATE TABLE IF NOT EXISTS  REG_VIDEOS(
    "name" VARCHAR(100),
    "km inicial" DOUBLE PRECISION,
    "km final" DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS  REG_RODOVIAS(
    "highway" VARCHAR(100),
    "km inicial" DOUBLE PRECISION,
    "km final" DOUBLE PRECISION
);

CREATE OR REPLACE VIEW  ABOVE_AVG_BURACO AS
SELECT "highway", "exp_km_calc", "Buraco"
FROM RESULTS
WHERE "Buraco" > (SELECT AVG("Buraco") FROM RESULTS);

CREATE OR REPLACE VIEW  ABOVE_AVG_REMENDO AS
SELECT "highway", "exp_km_calc", "Remendo"
FROM RESULTS
WHERE "Remendo" > (SELECT AVG("Remendo") FROM RESULTS);

CREATE OR REPLACE VIEW  ABOVE_AVG_TRINCA AS
SELECT "highway", "exp_km_calc", "Trinca"
FROM RESULTS
WHERE "Trinca" > (SELECT AVG("Trinca") FROM RESULTS);
