# Crie um programa que solicite um número inteiro e mostre sua tabuada de 1 até 10. 

import os
os.system('cls')

numero = int(input('Digite um número inteiro para ver sua tabuada: '))

try:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")