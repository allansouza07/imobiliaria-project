import pandas as pd

#IMPORTANDO OS DADOS DA TABELA
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

"""

print(dados['Valor'].mean(numeric_only = True))
preco = round(dados.groupby('Tipo')[['Valor']].mean(numeric_only = True).sort_values('Valor'),2)
print(preco)
#print(preco.plot(kind='barh', figsize=(14, 10), color ='purple'))
print(dados.Tipo.unique())
dados.query(Tipo == tipo)
"""




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

def shape_array(url):
    """
    Essa função revela quantas linhas e colunas tem a variável
    """
    return url.shape

def column_array(url):
    """
    Essa função revela quais são as colunas da tabela
    """
    return url.columns

def info_array(url):
    """
    Essa função revela o tipo de cada coluna da tabela
    """
    return url.info()

def mean_columns(url):
    """
    Essa função retorna a média da coluna de uma tabela
    """
    return round(url.mean(numeric_only=True),2)


dados_gerais = visualizar_dados(dados)
primeiros_elementos = primeiras_linhas(dados,10)
ultimos_elementos = ultimas_linhas(dados, 5)
formato_array = shape_array(dados)
colunas_array = column_array(dados)
informacoes_array = info_array(dados)
valores_quarto = dados[['Quartos','Valor']]
media_array = mean_columns(dados['Valor'])

print(media_array)
dados.query('Tipo' == 'Comercial')
