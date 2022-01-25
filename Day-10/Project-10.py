from art import logo
from functions import equacao
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')



print(logo)

loop = True

while loop == True:
    n1 = float(input("What's the first number? "))
    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("Pick an operation: ")
    n2 = float(input("What's the next number: "))
    result = equacao(n1,n2,operation)
    print(f"{n1} {operation} {n2} = {result}")
    continues = "y"

    while continues == "y":
        continues = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if continues == "y":
            new_result = result
            operation = input("Pick an operation: ")
            new_number = float(input("What's the next number:"))
            result = equacao(new_result, new_number, operation)
            print(f"{new_result} {operation} {new_number} = {result}")
        else:
            continues = "f"
            clear()





