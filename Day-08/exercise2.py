import sympy

def calc_prime_number(number):
    if sympy.isprime(number) == True:
        print(f"O numero {number} é primo")
    else:
        print(f"O número {number} não é primo")


numero = int(input("Digite um numero: "))

calc_prime_number(numero)
