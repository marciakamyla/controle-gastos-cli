from src.banco import (
    adicionar_gasto,
    listar_gastos,
    remover_gasto,
    calcular_total
)

def adicionar_gasto_menu():
    descricao = input("Digite a descrição do gasto: ")

    try:
        valor = float(input("Digite o valor do gasto: "))
    except ValueError:
        print("Valor inválido!")
        return

    data_gasto = input("Digite a data (AAAA-MM-DD): ")

    adicionar_gasto(descricao, valor, data_gasto)

    print("✅ Gasto adicionado com sucesso!")


def listar_gastos_menu():
    gastos = listar_gastos()

    if not gastos:
        print("Nenhum gasto registrado.")
        return

    print("\n--- Lista de Gastos ---")

    for gasto in gastos:
        print(
            f"ID: {gasto[0]} | "
            f"Descrição: {gasto[1]} | "
            f"Valor: R$ {gasto[2]} | "
            f"Data: {gasto[3]}"
        )


def remover_gasto_menu():
    listar_gastos_menu()

    try:
        id_gasto = int(input("\nDigite o ID do gasto para remover: "))

        remover_gasto(id_gasto)

        print("✅ Gasto removido!")

    except ValueError:
        print("ID inválido!")


def calcular_total_menu():
    total = calcular_total()

    print(f"\n💰 Total gasto: R$ {total}")


def menu():
    while True:
        print("\n--- Controle de Gastos ---")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Remover gasto")
        print("4. Ver total")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_gasto_menu()

        elif opcao == "2":
            listar_gastos_menu()

        elif opcao == "3":
            remover_gasto_menu()

        elif opcao == "4":
            calcular_total_menu()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()