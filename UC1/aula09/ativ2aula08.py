# Calculadora de IMC


def calcular_imc(peso, altura):
    '''
    Algoritimo para se calcular o IMC.
    ''' 
       
    IMC = (peso / (altura * altura))
    return IMC





def obter_classificacao(IMC):
    '''
    Algoritimo de classificação do IMC
    '''
    '''
    Valores de Referência:
    ■ Menor que 18.5: "Abaixo do peso"
    ■ 18.5 a 24.9: "Peso normal"
    ■ 25.0 a 29.9: "Sobrepeso"
    ■ 30.0 ou mais: "Obesidade"
    '''
    
    match IMC:
        case IMC if IMC < 18.5:
            print("Abaixo do peso")
        case IMC if IMC >= 18.5 and IMC <= 24.9:
            print("Peso normal")
        case IMC if IMC >= 25.00 and IMC <=29.99:
            print("Sobrepeso")
        case IMC if IMC >= 30.00:
            print("Obesidade")
        case _:
            print("Fora do valor de referência")
    return 


obter_classificacao(calcular_imc(101,2.00))
print(calcular_imc(101,2.00))