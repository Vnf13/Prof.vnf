# ======================================================
# INTRODUÇÃO
# ======================================================

# Neste projeto iremos analisar um conjunto de dados
# utilizando as principais bibliotecas de Análise de Dados.

# Importa a biblioteca Pandas e cria o apelido "pd".
# O Pandas será utilizado para carregar, organizar e analisar os dados.
import pandas as pd

# Importa o Matplotlib para criar e exibir gráficos.
import matplotlib.pyplot as plt

# ======================================================
# CARREGAMENTO DOS DADOS
# ======================================================

# Lê o arquivo "league.csv" e armazena seus dados
# na variável "df" (DataFrame).
df = pd.read_csv("league.csv")

# ======================================================
# EXPLORAÇÃO DOS DADOS
# ======================================================

# Exibe as 5 primeiras linhas da tabela.
df.head()

# Mostra informações gerais da tabela.
df.info()

# Exibe estatísticas das colunas numéricas.
df.describe()

# ======================================================
# LIMPEZA DOS DADOS
# ======================================================

# Conta quantos valores nulos existem em cada coluna.
df.isnull().sum()

# Substitui todos os valores nulos por 0.
df = df.fillna(0)

# ======================================================
# ANÁLISE DOS DADOS
# ======================================================

# Agrupa os dados pela coluna "Lane"
# e calcula a média da coluna "WinRate".
media_lane = df.groupby("Lane")["WinRate"].mean()

# ======================================================
# VISUALIZAÇÃO DOS DADOS
# ======================================================

# Cria um gráfico de barras utilizando apenas o Matplotlib.
plt.bar(media_lane.index, media_lane.values)

# Define o título do gráfico.
plt.title("Taxa média de vitória por Lane")

# Define o nome do eixo X.
plt.xlabel("Lane")

# Define o nome do eixo Y.
plt.ylabel("Win Rate (%)")

# Exibe o gráfico na tela.
plt.show()

# ======================================================
# CONCLUSÃO
# ======================================================

# Após analisar os dados e visualizar os gráficos,
# podemos interpretar os resultados e tirar conclusões
# sobre o conjunto de dados analisado.
