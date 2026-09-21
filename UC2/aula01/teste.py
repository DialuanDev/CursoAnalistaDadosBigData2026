import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  




#Nomear as variaveis de DataFrame para melhor entendimento
df_transacoes = pd.read_excel("base_invest.xlsx", sheet_name='Transacoes')
df_ativo = pd.read_excel("base_invest.xlsx", sheet_name='Ativo')


# 1. Quais são as máximas e mínimas de operação de compra e venda das transações?

# # Para encontrar as máximas e mínimas de operação de compra e venda das transações, podemos filtrar o DataFrame `df_transacoes` com base na coluna 'operacao' e, em seguida, usar os métodos `max()` e `min()` para obter os valores desejados.
# df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
# df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']

# #Use .max() e .min() para encontrar os valores máximos e mínimos de preço para as operações de compra e venda
# max_compra_preco = df_compra['preco'].max()
# min_compra_preco = df_compra['preco'].min()

# max_venda_preco = df_venda['preco'].max()
# min_venda_preco = df_venda['preco'].min()

# print("Máximo preço de compra:", max_compra_preco)
# print("Mínimo preço de compra:", min_compra_preco)

# print("Máximo preço de venda:", max_venda_preco)
# print("Mínimo preço de venda:", min_venda_preco)

#2. Qual CNPJ temm o ativo de maior valor?

# Primeiro, vamos calcular o valor total de cada transação multiplicando a quantidade pelo preço. Em seguida, podemos agrupar os dados por CNPJ e somar os valores totais para encontrar o CNPJ com o ativo de maior valor.
df_transacoes['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']

# Em seguida, podemos agrupar os dados por CNPJ e somar os valores totais para encontrar o CNPJ com o ativo de maior valor.
valor_por_ativo = df_transacoes.groupby('id_ativo')['valor_total'].sum()

# Agora, podemos encontrar o CNPJ com o maior valor total usando o método `idxmax()`, que retorna o índice (CNPJ) do valor máximo.
id_ativo_maior_valor = valor_por_ativo.idxmax()
print("CNPJ com o ativo de maior valor:", id_ativo_maior_valor)

# Para obter o CNPJ correspondente ao ativo de maior valor, podemos usar o `id_ativo_maior_valor` para filtrar o DataFrame `df_ativo` e obter o CNPJ associado a esse ativo. Aqui está como fazer isso:
cnpj_maior_valor = df_ativo[df_ativo['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]
print("CNPJ correspondente ao ativo de maior valor:", cnpj_maior_valor)

# 3. Qual valor total em transações de cada participante?

# Podemos agrupar os dados por 'id_participante' e somar os valores totais das transações para cada participante. Aqui está como fazer isso:
id_participante_valor_total = df_transacoes.groupby('id_participante')['valor_total'].sum()
print("Valor total em transações de cada participante:")
print(id_participante_valor_total)   



print(df_transacoes.head())  # Exibe as primeiras linhas do DataFrame df_transacoes
print(df_transacoes.tail())  # Exibe as últimas linhas do DataFrame df_transacoes