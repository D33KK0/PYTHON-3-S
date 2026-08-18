# *Questão 3:* Crie uma variável chamada temperatura e atribua um valor a ela. Escreva um
# código que imprima "Está frio" se a temperatura for menor que 15, "Está agradável" se es�ver
# entre 15 e 25, e "Está quente" se for maior que 25.

import os

os.system('cls' if os.name == 'nt' else 'clear')

temperatura = float(input("Digite a temperatura: "))

if temperatura < 15:
    print("Está frio")
elif temperatura > 14 and temperatura <= 25:
    print("Está agradável")
else:
    print("Está quente")