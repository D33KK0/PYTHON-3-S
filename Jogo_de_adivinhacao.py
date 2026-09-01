# Gere um número aleatório entre 1 e 20. Em um w h i l e T r u e , peça palpites até que o usuário
# acerte. Informe se cada palpite foi maior ou menor que o número sorteado, conte as tentativas e
# encerre com break quando houver acerto.

import random

numero_sorteado = random.randint(1, 20)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite (entre 1 e 20): "))
    tentativas += 1

    if palpite == numero_sorteado:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_sorteado:
        print("Seu palpite foi menor que o número sorteado.")
    else:
        print("Seu palpite foi maior que o número sorteado.")