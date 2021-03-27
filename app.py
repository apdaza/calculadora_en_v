from flask import Flask
from calculadora import Calculadora

app = Flask(__name__)

@app.route('/operacion/<operador>/<int:valor1>/<int:valor2>')
def operacion(operador, valor1, valor2):
    calculadora = Calculadora()
    calculadora.valor1 = valor1
    calculadora.valor2 = valor2
    if operador == '+':
        calculadora.sumar()
        resultado = calculadora.resultado
    elif operador == '-':
        calculadora.restar()
        resultado = calculadora.resultado
    else:
        resultado = None

    return str(valor1) + " " + operador + " " + str(valor2) + " = " + str(resultado)
    


if __name__ == '__main__':
    app.run(debug=True)