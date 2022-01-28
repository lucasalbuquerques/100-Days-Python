import random
from art import logo


def set_difficulty(level):
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("I didn't recognize your option, so it will be the 'easy' option ")
        return 10


def guess_game():
    awnser = random.randint(1,100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()
    attempt = set_difficulty(level)

    contador = 0

    while contador != attempt:
        print(f"You have {attempt - contador} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == awnser:
            print(f"You got it! The awnser was {guess}")
            contador = attempt - 1
        elif guess < awnser:
            if contador == attempt - 1:
                print("Too low")
                print("You've run out of guesses, you lose.")
            else:
                print("Too low.")
                print("Guess again.")
        elif guess > awnser:
            if contador == attempt - 1:
                print("Too high")
                print("You've run out of guesses, you lose.")
            else:
                print("Too high.")
                print("Guess again.")
        contador = contador + 1

guess_game()


