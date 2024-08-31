import pandas as pd
import os 
import glob

#Lê e consolida arquivos json - retornando um Dataframe
def extrair_dados(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True) #ignore_index = True, cria novos índices para a lista completa
    return df_total



def calcula_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


def load_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados_consolidados.csv")
        if formato == 'parquet':
            df.to_csv("dados_consolidados.parquet")





if __name__ == "__main__":
    pasta = "data"
    listaVendas = extrair_dados(path=pasta)
    totalVendas = calcula_kpi_total_vendas(listaVendas)
    formatoArquivos: list = ['csv', 'parquet']
    load_dados(totalVendas, formatoArquivos)

