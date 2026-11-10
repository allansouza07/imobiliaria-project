import pandas as pd
import matplotlib.pyplot as plt
from functions import visualizar_dados, primeiras_linhas, ultimas_linhas, shape_array, column_array,info_array, mean_columns, grafico_valor, grafico_percentual, bairros_apartamentos, verificacao_nulos,valores_nulos, eliminar_nulos

#IMPORTANDO OS DADOS DA TABELA
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

df_preco_tipo = (
    dados.groupby('Tipo')[['Valor']]
    .mean()
    .sort_values('Valor')
)
porcentos = dados.Tipo.value_counts(normalize= True).to_frame().sort_values('Tipo')
"""

print(dados['Valor'].mean(numeric_only = True))
preco = round(dados.groupby('Tipo')[['Valor']].mean(numeric_only = True).sort_values('Valor'),2)
print(preco)
#print(preco.plot(kind='barh', figsize=(14, 10), color ='purple'))
print(dados.Tipo.unique())
dados.query(Tipo == tipo)

print()
"""
dados_gerais = visualizar_dados(dados)
primeiros_elementos = primeiras_linhas(dados,10)
ultimos_elementos = ultimas_linhas(dados, 5)
formato_array = shape_array(dados)
colunas_array = column_array(dados)
informacoes_array = info_array(dados)
valores_quarto = dados[['Quartos','Valor']]
media_array = mean_columns(dados['Valor'])
visualizacao_grafico = grafico_valor(df_preco_tipo)
porcentagem_grafico = grafico_percentual(porcentos)
bairros_com_mais_apartamentos = bairros_apartamentos(dados)
verificacao_valores_nulos = verificacao_nulos(dados)
substituicao_valores_nulos = valores_nulos(dados)
eliminacao_valores_nulos = eliminar_nulos(dados)


