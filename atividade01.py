# Crie uma variável chamada
# idade e atribua a ela um valor inteiro. Escreva
# uma estrutura condicional que imprima "Você é
# maior de idade" se a idade for maior ou igual a
# 18 e "Você é menor de idade" caso contrário.

import os

os.system('cls' if os.name == 'nt' else 'clear')

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")