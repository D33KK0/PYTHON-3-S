# *Questão 6:* Defina uma variável chamada número com um valor inteiro. Escreva um código
# que imprima "O número é par" se o número for par e "O número é ímpar" se for ímpar.

import os

os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")