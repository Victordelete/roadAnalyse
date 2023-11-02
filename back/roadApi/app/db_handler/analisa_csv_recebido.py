import pandas as pd
import os

import db_handler.conecta_banco_dados as connbd

"""
Função para análise do arquivo recebido com dados registrados em vídeo.

Recebe: arquivo csv com dados brutos de eventos.  
Retorna: arquivo csv com dados com km e rodovia (highway).
    Dados são gravados no banco de dados. 
"""
def analisa_csv_recebido(path):
    path_out = '/back/roadApi/static/_data/_data_out/'

    try:
        df = pd.read_csv(path)
        
        rodovias = df['highway'].unique()

        for rodovia in rodovias:
            counted_data = df[df['highway'] == rodovia]
            counted_data = counted_data.groupby(['highway','exp_km_calc', 'item']).size().unstack(fill_value=0)
            
            arquivo_path =  os.getcwd() +path_out+ str(rodovia) + '.csv'

            counted_data.to_csv(arquivo_path,index=True)

            connbd.registra_resultado(arquivo_path)
    
    except Exception as error:
        print(f"Error: '{error}'")
        return False


"""
Função análisa arquivo recebido para preenchimento de tabelas auxiliares. 
    Recebe: path do arquivo recebido. 
    Retorna: True/False se Sucesso/Falha. 
"""
def preenche_tabelas_auxiliares(path):
    try:
        df = pd.read_csv(path)

        max_exp_km = df.groupby('highway')['exp_km_calc'].max().reset_index()
        min_exp_km = df.groupby('highway')['exp_km_calc'].min().reset_index()
        max_exp_km = max_exp_km.rename(columns={'exp_km_calc': 'km final'})
        min_exp_km = min_exp_km.rename(columns={'exp_km_calc': 'km inicial'})

        reg_rodovias = pd.merge(min_exp_km, max_exp_km, how = 'inner', on = 'highway')

        max_exp_km = df.groupby('name')['exp_km_calc'].max().reset_index()
        min_exp_km = df.groupby('name')['exp_km_calc'].min().reset_index()
        max_exp_km = max_exp_km.rename(columns={'exp_km_calc': 'km final'})
        min_exp_km = min_exp_km.rename(columns={'exp_km_calc': 'km inicial'})

        reg_videos = pd.merge(min_exp_km, max_exp_km, how = 'inner', on = 'name')

        connbd.registra_resultado_auxiliar(reg_rodovias, reg_videos)

        return True

    except Exception as error:
        print(f"Error: '{error}'")
        return False 