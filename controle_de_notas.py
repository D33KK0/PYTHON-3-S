# Crie uma lista vazia. Use w h i l e T r u e para cadastrar notas até que o usuário digite -1 . Depois do
# encerramento, utilize um for para mostrar cada nota cadastrada. Exiba também a quantidade, a
# média, a maior nota, a menor nota e as notas em ordem decrescente.

notas = []
while True:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

if notas:
    print("\nNotas cadastradas:")
    for i, nota in enumerate(notas, start=1):
        print(f"{i}. {nota}")

    print(f"\nQuantidade de notas: {len(notas)}")
    print(f"Média das notas: {sum(notas) / len(notas):.2f}")
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}")
    notas.sort(reverse=True)
    print("Notas em ordem decrescente:")
    for i, nota in enumerate(notas, start=1):
        print(f"{i}. {nota}")
else:
    print("Nenhuma nota foi cadastrada.")