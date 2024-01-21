import json

# Função para carregar tarefas do arquivo JSON
def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função para salvar tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=2)

# Função para exibir as tarefas na tela
def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas, nova_tarefa):
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f'Tarefa "{nova_tarefa}" adicionada com sucesso!')

# Função para remover uma tarefa com base no índice
def remover_tarefa(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefa_removida = tarefas.pop(indice - 1)
        salvar_tarefas(tarefas)
        print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
    else:
        print("Índice inválido. Nenhuma tarefa removida.")

# Função principal que gerencia o menu
def main():
    # Carrega as tarefas existentes do arquivo JSON
    tarefas = carregar_tarefas()

    while True:
        print("\nMenu:")
        print("1. Mostrar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Remover Tarefa")
        print("4. Sair")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == '1':
            mostrar_tarefas(tarefas)
        elif escolha == '2':
            nova_tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefa(tarefas, nova_tarefa)
        elif escolha == '3':
            mostrar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a ser removida: "))
            remover_tarefa(tarefas, indice)
        elif escolha == '4':
            print("Saindo. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
