tarefas = []

def adicionar_tarefa():
    nome = input("Digite a tarefa: ")
    tarefas.append({"nome": nome, "concluida": False})
    print("Tarefa adicionada!")

def listar_tarefas():
    print("\n--- MINHAS TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['nome']} - {status}")

def concluir_tarefa():
    listar_tarefas()
    numero = int(input("Número da tarefa: "))
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        print("Tarefa concluída!")
    else:
        print("Número inválido.")

while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "0":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida!")
