# Crie uma lista vazia. Utilize for com range(5) para pedir cinco produtos ao usuário e adicionar
# cada um com append() . Ao final, exiba a lista completa e a quantidade de produtos cadastrados.

produtos = []
for i in range(5):
    produtos.append(input(f"Digite o nome do produto {i + 1}: "))
    print(f"Produtos cadastrados: {produtos}")
print(f"Quantidade de produtos cadastrados: {len(produtos)}")