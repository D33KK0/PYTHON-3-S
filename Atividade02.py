# Escreva um programa que peça ao usuário
# para inserir sua idade. O programa deve
# classificar a pessoa em uma das seguintes
# categorias: "Criança" (0-12 anos),
# "Adolescente" (13-17 anos), "Adulto" (18-59
# anos), ou "Idoso" (60 anos ou mais).

import math
import os

os.system('cls' if os.name == 'nt' else 'clear')

idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida")

elif idade < 13:
    print("Você é uma Criança")

elif idade < 18:
    print("Você é um Adolescente")

elif idade < 60:
    print("Você é um Adulto")

else:
    print("Você é um Idoso")
