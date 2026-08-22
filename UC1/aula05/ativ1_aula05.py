
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota_optativa = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 - 1) / 2 
print(f"A média das duas notas é: {media:.2f}")

if nota_optativa > 0:
    if nota_optativa > nota1:
        media = (nota_optativa + nota2) / 2
    elif nota_optativa > nota2:
        media = (nota1 + nota_optativa) / 2

print(f"A média das duas notas é: {media:.2f}")