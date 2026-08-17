# x = 100
# y = 99.9
# print("x é maior que y?", x > y)
# print("x é igual a y?", x == y)
# resposta = x > y
# print("Resposta:", resposta)
# print(type(resposta))

# tem_carteira = True
# idade = 18
# tem_carro = False
# pode_dirigir = idade >= 18 and tem_carteira
# print("Pode dirigir?", pode_dirigir)
# print("Pode dirigir e tem carro?", pode_dirigir and tem_carro)

# # # # # # frase = "Python é divertido"
# # # # # # print(frase.upper())
# # # # # # nova_frase = frase.replace("divertido", "poderoso")
# # # # # # print(nova_frase)

# # # # # # contador = 0
# # # # # # contador += 5 # contador=contador+5
# # # # # # contador -= 2 # contador=contador-2
# # # # # # contador *= 3 # contador=contador*3
# # # # # # print("Valor final do contador:", contador)

# cnh = True
# bebidinha = False

# posso_dirigir = cnh and bebidinha
# print("Posso dirigir?", posso_dirigir)

# busaum = False
# trenzin = False 

# venho_pra_aula = busaum or trenzin
# print(venho_pra_aula)

locomocao = input("Qual é o seu meio de locomoção?  ")
choveu = True 

if choveu and locomocao == "moto":
    resultado = "Tô todo molhado :("
elif not choveu and locomocao == "moto":
    resultado = "to seco e feliz :)"
else:
    resultado = "Tô sequinho :)"

print(resultado)    