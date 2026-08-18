# *Questão 4:* Defina duas variáveis, a e b, com valores inteiros. Use uma estrutura
# condicional para verificar se a é maior que b. Se for, imprima "A é maior que B", caso contrário,
# imprima "B é maior ou igual a A".

import os

os.system('cls' if os.name == 'nt' else 'clear')

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A > B:
    print("A é maior que B")
else:
    print("B é maior ou igual a A")
    