gastos = []

def adicionar_gasto():
    descricao = input("Digite a descrição do gasto: ")
    valor = float(input("Digite o valor do gasto: "))

    if valor < 0:
        print("Valor inválido!")
        return

    gastos.append({"descricao": descricao, "valor": valor})
    print("Gasto adicionado com sucesso!")

def listar_gastos():
    if not gastos:
        print("Nenhum gasto registrado.")
        return

    for i, gasto in enumerate(gastos):
        print(f"{i} - {gasto['descricao']} | R$ {gasto['valor']}")

def remover_gasto():
    listar_gastos()
    try:
        indice = int(input("Digite o índice do gasto para remover: "))
        gastos.pop(indice)
        print("Gasto removido!")
    except Exception:
        print("Índice inválido!")

def calcular_total():
    total = sum(g["valor"] for g in gastos)
    print(f"Total gasto: R$ {total}")

def menu():
    while True:
        print("\n--- Controle de Gastos ---")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Remover gasto")
        print("4. Ver total")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_gasto()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            remover_gasto()
        elif opcao == "4":
            calcular_total()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()