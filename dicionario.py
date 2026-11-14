import pandas as pd
from functions import visualizar_dados, primeiras_linhas, ultimas_linhas, shape_array, column_array,info_array, mean_columns, grafico_valor, grafico_percentual, bairros_apartamentos, verificacao_nulos,valores_nulos, eliminar_nulos,analisar_quartos_unicos,analisar_quartos,salvar_dados, criar_coluna_valor_mensal,descricao_imoveis,tem_suite

#IMPORTANDO OS DADOS DA TABELA
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

df_preco_tipo = (
    dados.groupby('Tipo')[['Valor']]
    .mean()
    .sort_values('Valor')
)
porcentos = dados.Tipo.value_counts(normalize= True).to_frame().sort_values('Tipo')


funcoes = [
    {'nome': 'Dados Gerais', 'funcao': visualizar_dados(dados)},
    {'nome': 'Primeiros elementos da tabela', 'funcao': primeiras_linhas(dados, 10)},
    {'nome': 'Últimos elementos da tabela', 'funcao': ultimas_linhas(dados, 5)},
    {'nome': 'Formato do array', 'funcao': shape_array(dados)},
    {'nome': 'Colunas do array', 'funcao': column_array(dados)},
    {'nome': 'Informações do array', 'funcao': info_array(dados)},
    {'nome': 'Valores de Quartos e Valor', 'funcao': dados[['Quartos', 'Valor']]},
    {'nome': 'Média da coluna Valor', 'funcao': mean_columns(dados['Valor'])},
    {'nome': 'Gráfico de valores', 'funcao': grafico_valor(df_preco_tipo)},
    {'nome': 'Gráfico de porcentagem', 'funcao': grafico_percentual(porcentos)},
    {'nome': 'Bairros com mais apartamentos', 'funcao': bairros_apartamentos(dados)},
    {'nome': 'Verificação de valores nulos', 'funcao': verificacao_nulos(dados)},
    {'nome': 'Substituição de valores nulos', 'funcao': valores_nulos(dados)},
    {'nome': 'Eliminação de valores nulos', 'funcao': eliminar_nulos(dados)},
    {'nome': 'Análise de quartos únicos', 'funcao': analisar_quartos_unicos(dados)},
    {'nome': 'Análise de quartos', 'funcao': analisar_quartos(dados)},
    {'nome': 'Salvar dados', 'funcao': salvar_dados(dados)},
    {'nome': 'Valor mensal', 'funcao': criar_coluna_valor_mensal(dados)},
    {'nome': 'Descrição dos imóveis', 'funcao': descricao_imoveis(dados)},
    {'nome': 'Verificação de suítes', 'funcao': tem_suite(dados)}
]

