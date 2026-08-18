# *Questão 5:* Crie uma variável senha e atribua um valor a ela. U�lize uma estrutura
# condicional para verificar se a senha é igual a "python123". Se for, imprima "Acesso permi�do",
# senão imprima "Acesso negado".

import os

os.system('cls' if os.name == 'nt' else 'clear')

senha = input("Digite a senha: ")

if senha == "python123":
    print("Acesso permitido")
else:
    print("Acesso negado")
