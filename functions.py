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
        color='purple',
        title = 'Tipos imobiliários com maiores valores'
    )
    return plt.show()

def grafico_percentual(url):
    """
    Essa função retorna um gráfico percentual da variável 'porcentos', que revela a porcentagem de cada categoria da coluna Tipo
    """
    url.plot(kind='bar', figsize=(14,18), color = 'blue',xlabel = 'Tipos', ylabel = 'Percentual', title='Porcentagem da presença de cada tipo em relação ao total')

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

def verificacao_nulos(dado):
    """
    Essa função retorna quantos valores são nulos em uma variável
    """
    return dado.isnull().sum()

def valores_nulos(dado):
    """
    Essa função retorna a substituição de todos os valores nulos de uma variável por 0
    """
    return dado.fillna(0)

def eliminar_nulos(dado):
    """
    Essa função elimina registros com valores nulos de uma variável
    """
    return dado.dropna(subset=['Valor', 'Condominio'], inplace=True)

def analisar_quartos_unicos(dado):
    """
    Essa função revela os apartamentos com quartos únicos e preços acima de 1200 da variável Dados
    """
    filtro1 = dado['Quartos'] == 1
    filtro2 = dado['Valor'] > 1200
    filtragem = filtro1 & filtro2

    return dado[filtragem]

def analisar_quartos(dado):
    """
    Essa função revela os apartamentos com 2 quartos ou mais, que custem
    """
    filtragem = dado.query('Quartos >= 2 and Valor < 3000 and Area > 70')
    return filtragem
    