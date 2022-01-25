def somar(a, b):
    """Retorna a soma de dois numeros"""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de dois numeros"""
    return a - b


def dividir(a, b):
    """Retorna a divisão de dois numeros"""
    return a / b


def multiplicar(a, b):
    """Retorna a multiplicação de dois numeros"""
    return a * b

def equacao(n1,n2,operacao):
    if operacao == "+":
        return somar(n1, n2)
    elif operacao == "-":
        return subtrair(n1, n2)
    elif operacao == "*":
        return multiplicar(n1, n2)
    elif operacao == "/":
        return dividir(n1, n2)
