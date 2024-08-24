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


def filtrarProdutos(lista: list[dict], situacao: str) -> list[dict]:
    """Funcao que filtra situacao do produto"""
    listaFiltrada = []
    for produto in lista:
        if produto.get("entregue") == situacao:
            listaFiltrada.append(produto)
    return listaFiltrada


arquivoFiltrado: list[dict]
arquivoFiltrado = filtrarProdutos(arquivoVendas, situacao = "False") #Situação



def somaValoresFiltrados(lista: list[dict]) -> int:
    soma: int = 0;
    for produto in lista:
        soma = soma + int(produto.get("valor"));
    return soma


somaValores: int; 
somaValores = somaValoresFiltrados(arquivoVendas)


# print(arquivoVendas)
print(arquivoVendas)
print(f'A soma Total dos produtos é: {somaValores}')






