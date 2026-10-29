import pandas as pd

#IMPORTANDO OS DADOS DA TABELA
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

def visualizar_dados(url):
    """
    Essa função permite a visualização geral dos dados
    """
    return url

def primeiras_linhas(url, qtd):
    """
    Essa função permite a visualização das X primeiras linhas da tabela
    """
    return url.head(qtd)

def ultimas_linhas(url,qtd):
    """
    Essa função permite a visualização das X últimas linhas da tabela
    """
    return url.tail(qtd)

dados_gerais = visualizar_dados(dados)
primeiros_elementos = primeiras_linhas(dados,10)
ultimos_elementos = ultimas_linhas(dados, 5)

print(ultimos_elementos)