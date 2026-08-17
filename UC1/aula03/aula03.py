nome = "Maria"           # str: texto, isto é, uma cadeia de caracteres
idade = 30               # int: número inteiro
preco = 19.99            # float: número com casas decimais
esta_matriculada = True  # bool: valor lógico, True ou False
notas = [8.0, 7.5]       # list: coleção ordenada e modificável
aluno = ("Maria", 30)    # tuple: coleção ordenada e imutável
disciplinas = {"Python", "Lógica"}  # set: conjunto sem elementos repetidos
cadastro = {"nome": "Maria", "idade": 30}  # dict: pares de chave e valor

# A função type() permite consultar o tipo de um dado.
print(type(nome))
print(type(idade))
print(type(preco))


# Cada nota fica armazenada em uma variável diferente.
nota_1 = 2
nota_2 = 4

# A média é calculada e armazenada em uma terceira variável.
media = (nota_1 + nota_2) / 2

print("===== RESULTADO =====")

print(f"Primeira nota: {nota_1:.1f}")
print(f"Segunda nota: {nota_2:.1f}")
print(f"Média: {media:.1f}")