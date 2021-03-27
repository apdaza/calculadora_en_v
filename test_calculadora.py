from calculadora import Calculadora

class TestCalculadora:

    def test_suma(self):
        calculadora = Calculadora()
        calculadora.valor1 = 5
        calculadora.valor2 = 2
        calculadora.sumar()
        assert calculadora.resultado == 7

    def test_resta(self):
        calculadora = Calculadora()
        calculadora.valor1 = 5
        calculadora.valor2 = 2
        calculadora.restar()
        assert calculadora.resultado == 3