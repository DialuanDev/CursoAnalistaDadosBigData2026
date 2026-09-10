## AULA 01 ##

import pandas as pd  # alias 'pd'
import numpy as np   # alias 'np'
import openpyxl


# numeros_impares = [43,55,1,3,11,27,109]
# numeros_seq = [2,3,4,5,6,6,7]

# serie_impares = pd.Series(numeros_impares)

# print(serie_impares)
# print(type(serie_impares))

# print(serie_impares.sum())
# print(serie_impares.mean())
# print(serie_impares.min())
# print(serie_impares.max())
# print(len(serie_impares))
# print(serie_impares.describe())
# print(serie_impares[serie_impares > 50])

# serie2_impares = pd.Series(
#     numeros_impares,
#     index = ["a","b","c","d","e","f","g"])

# print(serie2_impares)    

# filmes = {
#     'título': ["Lagoa Azul","Agente secreto", "Gênio Indomável"],
#     'categoria':["Romance", "Ação", "Drama"],
#     'ano': ["1980", "2025", "1997"]      # OBS.: caracterticas qualitativas usam aspas simples ou duplas por que não são números são carcteristicas dos filmes
# }

# tabela_filmes = pd.DataFrame(filmes)

# print(filmes)
# print(tabela_filmes)
# print(type(tabela_filmes))

# serie_impares = pd.Series(numeros_impares)
# print(serie_impares)

# quadrado_serie_impares = serie_impares * serie_impares
# print(quadrado_serie_impares)

### LEITURA DE ARQUIVOS XLSX ###
#variavel         #comando      #caminho do arquivo  #arqumentos de leitura
leitura_invest = pd.read_excel("base_invest.xlsx", sheet_name = 1 )

print(leitura_invest)

























