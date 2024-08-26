import pandas as pd
import os 
import glob

pasta = 'data'


def extrair_dados(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


print(extrair_dados(path=pasta))

