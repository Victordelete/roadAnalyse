import pandas as pd 
import pandas.io.sql as sqlio 
import psycopg2 
import os
from sqlalchemy import create_engine


db_params = {
    "database": "rodovias",
    "user": "postgres",
    "password": "3141592",
    "host": "localhost",
    "port": "5432"
}

"""
Função inicia a tabela no banco de dados postgres com as configurações. Deve ser chamado somente uma vez para inicialização. 
Recebe: 
Retorna: True se sucesso, false se erro. 
"""
def inicia_banco_dados():
    file = os.getcwd() + '/back/roadApi/app/db_handler/inicia_banco.sql'

    try: 
        conn = psycopg2.connect(**db_params)
    
        cursor = conn.cursor()

        try: 
            query = open(file, encoding="utf8").read()
        except Exception as error:
            print(f"Error: '{error}'")
            return False

        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as error:
        print(f"Error: '{error}'")
        return False
    
    return True

"""
Função registra no banco de dados os resultados obtidos para análise das rodovias.
Recebe: dataframe com os resultados da análise. 
Retorna: True se sucesso, falso se erro. 
"""
def registra_resultado(arquivo_path):
    try:
        df = pd.read_csv(arquivo_path)

        conn = psycopg2.connect(**db_params)

        engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

        df.to_sql('results', engine, if_exists="append", index=False)

        conn.close()

        return True
    
    except Exception as error:
        print(f"Error: '{error}'")
        return False

"""
Função realiza query no banco de dados para incidência máxima dos itens.
Recebe: rodovia.
Devolve: list com valor(es) do km(s) em que o item é máximo. 
"""
def query_km_max_item(rodovia, item):

    consulta_sql = f'SELECT "exp_km_calc" AS "KMS MAXIMO" FROM RESULTS WHERE "{item}" = (SELECT MAX("{item}") AS MAX_item FROM RESULTS WHERE "highway"=\'{rodovia}\' GROUP BY "highway") AND "highway"=\'{rodovia}\''
    
    try: 
        conn = psycopg2.connect(**db_params)

        cursor = conn.cursor()

        cursor.execute(consulta_sql)
        results = cursor.fetchall() 
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as error:
        print(f"Error: '{error}'")
        return False

    return results

"""
Função realiza consulta ao banco de dados, de arquivos com valor de tabela acima da média. 
Recebe: nome da tabela com view para esta consulta pronta (Buraco, Remendo, Trinca)
Devolve: list com resultado. 
"""
def consulta_km_acima_media(tabela):
    consulta_sql = f'SELECT * from ABOVE_AVG_{tabela};'
    
    try: 
        conn = psycopg2.connect(**db_params)

        cursor = conn.cursor()

        cursor.execute(consulta_sql)
        results = cursor.fetchall() 
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as error:
        print(f"Error: '{error}'")
        return False

    return results

"""
Registra as tabelas auxiliares. 
Recebe: dois dataframes com o valor das tabelas. 
Retorna: True/False se Sucesso/Falha. 
"""
def registra_resultado_auxiliar(reg_rodovias, reg_videos):
    try:
        conn = psycopg2.connect(**db_params)

        engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

        reg_rodovias.to_sql('reg_rodovias', engine, if_exists="append", index=False)
        reg_videos.to_sql('reg_videos', engine, if_exists="append", index=False)

        conn.close()

        return True
    
    except Exception as error:
        print(f"Error: '{error}'")
        return False


inicia_banco_dados()