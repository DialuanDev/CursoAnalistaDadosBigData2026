# Cálculo de Média Escolar para Vários Alunos:

from unittest import case


alunos = int(10)

for i in range(alunos):
    print("Digite a nota do", i + 1,"º aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota_optativa = float(input("Digite a terceira nota: "))

    if nota1 and nota2 > nota_optativa:
        nota_optativa = -1
        media = (nota1 + nota2 + nota_optativa) / 2 
    elif nota1 and nota_optativa > nota2:     
        media = (nota1 + nota_optativa) / 2
    else:
        media = (nota2 + nota_optativa) / 2

    match media:
        case media if media >= 6:
            print("A media final do", i + 1,"º aluno é: ", media, " - Aprovado")
        case media if media < 3:
            print("A media final do", i + 1,"º aluno é: ", media, " - Reprovado")
        case media if media >= 3 and media < 6:
            print("A media final do", i + 1,"º aluno é: ", media, " - Recuperação")