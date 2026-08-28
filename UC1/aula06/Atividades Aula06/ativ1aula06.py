alunos = 5
resultados = []

for i in range(alunos):
    print(f"\nDigite as notas do {i + 1}º aluno:")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota_optativa = float(input("Digite a nota optativa: "))

    
    if nota1 > nota_optativa and nota2 > nota_optativa:
        media = (nota1 + nota2) / 2
    elif nota1 > nota_optativa and nota_optativa > nota2:
        media = (nota1 + nota_optativa) / 2
    else:
        media = (nota2 + nota_optativa) / 2

    
    if media >= 6:
        situacao = "Aprovado"
    elif media < 3:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"

    resultado = f"Aluno {i + 1} - Média: {media:.1f} - {situacao}"
    print(resultado)

    resultados.append(resultado) 


print("\n===== RESULTADOS FINAIS =====")
for r in resultados:
    print(r)
