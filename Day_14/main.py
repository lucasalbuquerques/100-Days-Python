import random
import art
from game_data import data

def compare_follows(a, b, anwser, continues):
    if anwser == "b":
        if b["follower_count"] > a["follower_count"]:
            continues = True
            return continues
        else:
            continues = False
            return continues
    elif anwser == "a":
        if a["follower_count"] > b["follower_count"]:
            continues = True
            return continues
        else:
            continues = False
            return continues

def game():
    next_game = True
    while next_game == True:
        print(art.logo)
        score = 0
        continues = True


        a = random.choice(data)
        b = random.choice(data)
        print(f'Compare A: {a["name"]}, {a["description"]}, from {a["country"]}')
        print(art.vs)
        print(f'Compare A: {b["name"]}, {b["description"]}, from {b["country"]}')

        anwser = input("Who has more followers ? Type 'A' or 'B': ").lower()

        continues = compare_follows(a, b, anwser, continues)
        if continues == True:
            score = score + 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")

        while continues == True:
            a = b
            b = random.choice(data)
            print(f'Compare A: {a["name"]}, {a["description"]}, from {a["country"]}')
            print(art.vs)
            print(f'Against B: {b["name"]}, {b["description"]}, from {b["country"]}')
            anwser = input("Who has more followers ? Type 'A' or 'B': ").lower()
            continues = compare_follows(a, b, anwser, continues)
            if continues == True:
                score = score + 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
        next_game_anwser = input("Do you want play again? Type 'y' or 'n'").lower()
        if next_game_anwser == "y":
            next_game = True
        else:
            next_game = False

game()


