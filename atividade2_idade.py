# Crie um programa que solicite a idade de uma pessoa. 

try:
    while True:
        idade = int(input("Digite a sua idade: "))
        if idade >= 18:
            print("Maior de idade.")
            break
        else:
            print("Menor de idade.")
            break
      # Sai do loop se a idade for válida
except ValueError:  
    print("Por favor, digite apenas números inteiros válidos.")