
# impar_1 = 3
# impar_2 = 5 
# impar_3 = 13
# impar_4 = 27

# impares = []
# print(type(impares))
# impares = [3, 5, 13, 27]
# print(impares[-14])

# lista_01 = [12,"Pedro", 12.53343,"[{_^^{{}}}]", False,0,[2,4,6,8]]
# print(lista_01[6][2])

#Condicionais:

# lista_02 = ["Marcia"]

# if "Marcia" in lista_02:
#     print(lista_02)
# else:
#     print("Não está na lista")



# match lista_02:             
#     case ["Marcia"]:
#         print("Marcia está na lista")
#     case _:
#         print("Não está na lista")


#LOOPINGS:

#participantes = ["Isaque","Luana","Fernando","Bianca","Ana Paula"]

# for participantes in participantes:
#     print(participantes)

# partic_2 = "Hugo"
# participantes.append("Hugo")
# participantes.insert(2,partic_2)
# participantes.pop(1)
# participantes.remove("Hugo")
# participantes.reverse()
# participantes.count("Hugo")
# participantes.clear()

# print(participantes)

#Tuplas
# participantes = ("Isaque","Luana","Fernando","Bianca","Ana Paula")
# print(participantes, type(participantes))

#Sets:

# numeros_pares = {
#     202,
#     203,
#     204,
#     204,
#     205,
#     219,
#     291,
#     292,
#     202,
#     }

# print(numeros_pares, type(numeros_pares))

# numeros_impares = {111,111,112,291,291,205}

# print(numeros_pares.intersection(numeros_impares))

# numeros_pares.remove(205)
# numeros_pares.add(2)
# numeros_pares.update(4)
# print(numeros_pares)

#DICIONÁRIOS:

produtos = {
    "maça": 5.99,
    "laranja":4.79, 
}


# print(produtos, type(produtos))

print(produtos.items())
print(produtos.keys())
print(produtos.values())

produtos.get("laranja")
produtos2 = produtos.copy()

# produtos.pop("maça")
produtos2["maça"]=7.99

print(produtos2)

achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)