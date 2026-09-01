# Crie uma lista vazia e apresente continuamente o menu: 1 - Adicionar tarefa, 2 - Remover tarefa,
# 3 - Mostrar tarefas e 0 - Sair. Use w h i l e T r u e para manter o menu ativo, append() para
# adicionar, remove() para retirar e break para encerrar.

tarefas = []

while True:
    print("\nMenu de Gerenciamento de Tarefas:")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Mostrar tarefas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        if tarefas:
            tarefa = input("Digite a tarefa a ser removida: ")
            if tarefa in tarefas:
                tarefas.remove(tarefa)
                print("Tarefa removida com sucesso!")
            else:
                print("Tarefa não encontrada.")
        else:
            print("Não há tarefas para remover.")
    elif opcao == "3":
        if tarefas:
            print("Tarefas:")
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t}")
        else:
            print("Não há tarefas para mostrar.")
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")