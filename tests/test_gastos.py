import unittest
from src import main

class TestGastos(unittest.TestCase):

    def setUp(self):
        main.gastos.clear()

    def test_adicionar_gasto(self):
        main.gastos.append({"descricao": "Teste", "valor": 10})
        self.assertEqual(len(main.gastos), 1)

    def test_valor_negativo(self):
        valor = -5
        self.assertTrue(valor < 0)

    def test_calcular_total(self):
        main.gastos.append({"descricao": "A", "valor": 10})
        main.gastos.append({"descricao": "B", "valor": 20})
        total = sum(g["valor"] for g in main.gastos)
        self.assertEqual(total, 30)

if __name__ == "__main__":
    unittest.main()