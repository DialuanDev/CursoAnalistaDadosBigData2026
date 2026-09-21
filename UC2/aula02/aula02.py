import pandas as pd  # alias 'pd'
import numpy as np   # alias 'np'
import matplotlib.pyplot as plt


#LOC
#ILOC
#QUERY


filmes = {
    'título': ["Lagoa Azul","Agente secreto", "Gênio Indomável", "A freira", "Brinquedo Assassino", "Top Gun"],
    'categoria':["Romance", "Ação", "Drama", "Terror", "Comedia", "Aventura"],
    'ano': ["1980", "2025", "1997", "2022", "1995", "1986"],
    'faturamento': [6.5,4,5.5,3,9,7.2]  # OBS.: caracterticas quantitativas usam números
}

indices = ['A', 'B', 'C', 'D', 'E', 'F']
tabela_filmes = pd.DataFrame(filmes, index=indices)

print(filmes)
print(tabela_filmes)
print(type(tabela_filmes))

print("------------------------(iLoc)--------------------------------")
print(tabela_filmes.iloc[0]) # Acessa a primeira linha da tabela
print("--------------------------------------------------------")
print(tabela_filmes.iloc[1]) # Acessa a segunda linha da tabela
print("--------------------------------------------------------")
print(tabela_filmes.iloc[0,2]) # Acessa a primeira linha e a terceira coluna da tabela
print("--------------------------------------------------------")
print(tabela_filmes.iloc[-1]) # Acessa a última linha da tabela


print("------------------------(Loc)--------------------------------")

print(tabela_filmes.loc['A']) # Acessa a linha com índice 'A'
print("--------------------------------------------------------")
print(tabela_filmes.loc['B']) # Acessa a linha com índice 'B'
print("--------------------------------------------------------")
print(tabela_filmes.loc['C']) # Acessa a linha com índice 'C'
print("--------------------------------------------------------")


print("------------------------(Query)--------------------------------")
consulta1 = tabela_filmes.query("faturamento == 5.5") # Acessa as linhas com faturamento igual a 5.5
print(consulta1)


print("------------------------(Intervalos Iloc / Loc)--------------------------------")

print(tabela_filmes.iloc[1:3]) # Acessa as linhas de índice 0 a 2 (exclusivo do índice 3)
print("--------------------------------------------------------")
print(tabela_filmes.loc['B':'E']) # Acessa as linhas com índices 'B' a 'E' (inclusivo do índice 'E')
print("--------------------------------------------------------")