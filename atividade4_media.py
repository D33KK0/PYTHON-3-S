import os 

os.system('cls')

while True:
    try:
        nota1 = float(input('Digite a nota do aluno: '))
        nota2 = float(input('Digite a segunda nota do aluno: '))
        nota3 = float(input('Digite a terceira nota do aluno: '))
        
        media = (nota1 + nota2 + nota3) / 3
        
        print(f'A média do aluno é: {media:.2f}')
        if media >= 7:
            print('O aluno está aprovado.')
        else:
            print('O aluno está reprovado.')
        break 
    
    except ValueError:
        print("Por favor, digite apenas números válidos.")
