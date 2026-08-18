# 8. Crie um programa que peça ao usuário para inserir dois números e uma operação (adição,
# subtração, mul�plicação ou divisão). Realize a operação solicitada e exiba o resultado.

import os
os.system("cls")


A = int(input("Digite o n1: "))
B = int(input("Digite o n2: "))
OP = str(input("Digite o operação desejada ( +, -, /, *): "))

match OP:
    case "+":
        res= A + B
        
        print(f"O resultado da operação soma é {res}")
    case "*":
        res= A * B
        print(f"O resultado da operação multiplicação é {res}")
    case "-":
        res= A - B
        print(f"O resultado da operação substração é {res}")
    case "/":
        res= A/B
        print(f"O resultado da operação divisão é {res}")
    case _:
        print("Escolha inválida")