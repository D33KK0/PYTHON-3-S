# Crie uma lista vazia e utilize w h i l e T r u e para receber nomes. Cada nome deve ser incluído com
# append() . Quando o usuário digitar 'fim' , encerre com break . Depois, organize os nomes em
# ordem alfabética e mostre a lista e sua quantidade.

nomes = []
while True:
    nome = input("Digite o nome do convidado (ou 'fim' para encerrar): ")
    if nome == "fim":
        break
    nomes.append(nome)

nomes.sort()
print(f"Convidados confirmados: {nomes}")
print(f"Quantidade de convidados: {len(nomes)}")