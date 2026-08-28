#Cadastro Seletivo de Candidatos

ano = int(2026)
candidatos = int(5)
candidatos_validos = []
candidato = {}

for i in range(candidatos):
    print("Cadastro do", i + 1,"º candidato: ")
    ano_nascimento = int(input("Digite o ano de nascimento do candidato: "))
    idade = ano - ano_nascimento

    if idade < 18:
        print("Candidato não pode se candidatar, pois tem ", idade, " anos.")
    else:
        inscricao_nome = input("Digite o nome do candidato: ")
        inscricao_email = input("Digite seu email: ")
        inscricao_cidade = input("Digite sua cidade: ")
        candidato = {
            "Candidato": i + 1,
            "Nome": inscricao_nome,
            "Email": inscricao_email,
            "Cidade": inscricao_cidade
        }
        candidatos_validos.append(candidato)


print(candidatos_validos)

for y in candidatos_validos:
    print(y)    