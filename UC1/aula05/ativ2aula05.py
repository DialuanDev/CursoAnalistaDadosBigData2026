#Cadastro de Candidatos

ano = int(2026)
candidatos = int(12)

for i in range(candidatos):
    print("Cadastro do", i + 1,"º candidato: ")
    ano_nascimento = int(input("Digite o ano de nascimento do candidato: "))
    idade = ano - ano_nascimento

    if idade < 18:
        print("Candidato não pode se candidatar, pois tem ", idade, " anos.")
    else:
        inscricao = input("Digite o nome do candidato: \n" \
        "Digite o número do telefone do candidato: \n" \
        "Digite o e-mail do candidato: \n" \
        "Digite o endereço do candidato: \n" \
        "Digite o número do CPF do candidato: \n")

