import csv



"""Cria Função de Média de Valores"""
def somaValoresLista(lista: list):
    return sum(lista)/len(lista)




"""Cria Função de Leitura de CSV e retorna uma lista de dicionarios"""
def lerCsv(nomeArquivo: str) -> list[dict]:
    listaItens = [];
    with open(nomeArquivo, mode='r', encoding='utf-8') as arquivo:
        leituraArquivo = csv.DictReader(arquivo, delimiter=';')
        for itens in leituraArquivo:
            listaItens.append(itens)
    return listaItens




pathArquivo = 'vendas.csv'
arquivoVendas: list[dict]
arquivoVendas = lerCsv(pathArquivo)

print(arquivoVendas)
