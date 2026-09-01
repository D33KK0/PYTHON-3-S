# Peça seis números inteiros utilizando um laço for e armazene-os em uma lista. Depois, mostre a
# soma, o maior valor, o menor valor e os números em ordem crescente.

numeros = []

for i in range(6):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)
    
print(f"Soma dos números: {sum(numeros)}")
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")
print(f"Números em ordem crescente: {sorted(numeros)}")