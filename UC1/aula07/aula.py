#Funções

numb1 = float(input("Digite um numero: "))
numb2 = float(input("Digite um segundo numero: "))

operador = input("Informe: 1- para adição.  2 - para subtração.  3 - para multiplicação. 4 - para divisão. ")

match operador:
    case '1':
        print(f"resultado da soma: {numb1+numb2}")
    case '2':
        print(f"resultdao da subtração: {numb1-numb2}")

