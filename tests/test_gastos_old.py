import unittest


class TestGastos(unittest.TestCase):

    def test_valor_negativo(self):
        valor = -5
        self.assertTrue(valor < 0)

    def test_calculo_simples(self):
        valores = [10, 20]
        total = sum(valores)
        self.assertEqual(total, 30)


if __name__ == "__main__":
    unittest.main()