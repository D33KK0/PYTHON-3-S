# Crie um programa que solicite ao usuário dois números e mostre a soma deles. 
# O programa deve utilizar try/except para impedir que o programa seja encerrado caso o usuário digite algo que não seja um número.

try:
    while True:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        soma = numero1 + numero2
        print(f"A soma de {numero1} e {numero2} é: {soma}")
        break  # Sai do loop se a soma for realizada com sucesso
except ValueError:
    print("Por favor, digite apenas números válidos.")  