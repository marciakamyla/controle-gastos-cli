from src.banco import listar_gastos

gastos = listar_gastos()

for gasto in gastos:
    print(gasto)