import pandas as pd  # alias 'pd'
import numpy as np   # alias 'np'
import matplotlib.pyplot as plt

#Nomear as variaveis de DataFrame para melhor entendimento
df_transacoes = pd.read_excel("base_invest.xlsx", sheet_name='Transacoes')
df_ativo = pd.read_excel("base_invest.xlsx", sheet_name='Ativo')

#Dados exemplo (Quartils)

# dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])
# print(dados)

# # Calculando os quartis
# q1 = np.percentile(dados, 25) # Calcula o primeiro quartil (25º percentil)
# q2 = np.percentile(dados, 50) # Calcula o segundo quartil (50º percentil ou mediana)
# q3 = np.percentile(dados, 75) # Calcula o terceiro quartil (75º percentil)

# # Imprimindo os quartis
# print("Primeiro Quartil (Q1):", q1)
# print("Segundo Quartil (Q2, Mediana):", q2)
# print("Terceiro Quartil (Q3):", q3)


print(df_transacoes.head())  # Exibe as primeiras 5 linhas do DataFrame df_transacoes
print(df_transacoes.tail())  # Exibe as últimas 5 linhas do DataFrame df_transacoes

q1_preco = df_transacoes['preco'].quantile(0.25)  # Primeiro quartil (25%)
q2_preco = df_transacoes['preco'].quantile(0.50)  # Segundo quartil (50% ou mediana)
q3_preco = df_transacoes['preco'].quantile(0.75)  # Terceiro quartil (75%)

print("Primeiro Quartil (Q1) do preço:", q1_preco)
print("Segundo Quartil (Q2, Mediana) do preço:", q2_preco)
print("Terceiro Quartil (Q3) do preço:", q3_preco)

# Contagem de operações 
contagem_operacoes = df_transacoes['operacao'].value_counts()

#Criar um gráfico de barras para visualizar a contagem de operações
contagem_operacoes.plot(kind='barh', title= 'Tipos de Operação')
# Tipo de gráfico: 'bar' para gráfico de barras verticais, 'barh' para gráfico de barras horizontais, 'axvline' para linha vertical, 'axhline' para linha horizontal, 'scatter' para gráfico de dispersão, 'pie' para gráfico de pizza, 'hist' para histograma, 'box' para boxplot, 'area' para gráfico de área, 'hexbin' para gráfico hexagonal, 'kde' para estimativa de densidade kernel, 'line' para gráfico de linha.

#Mostrar o gráfico

plt.show()