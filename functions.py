import pandas as pd
import matplotlib.pyplot as plt

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

def grafico_valor(url):
    """
    Essa função retorna, especificamente, um gráfico dos valores da variável 'dados'
    """
    
    url.plot(
        kind='barh',
        figsize=(10, 5),
        color='purple'
    )
    return plt.show()

def grafico_percentual(url):
    """
    Essa função retorna um gráfico percentual da variável 'porcentos'
    """
    url.plot(kind='bar', figsize=(14,18), color = 'blue',xlabel = 'Tipos', ylabel = 'Percentual')

    return plt.show()

def bairros_apartamentos(dado):
    """
    Essa função retorna um gráfico da quantidade de apartamentos por bairro da variável 'dados'
    """
    url = dado.query("Tipo == 'Apartamento'")
    apt_bairros = url['Bairro'].value_counts()
    apt_bairros.plot(
        kind='bar', figsize=(14,8),color='blue',xlabel ='Bairros', ylabel = 'Apartamentos',title='Bairros com mais apartamentos'
    )
    return plt.show()