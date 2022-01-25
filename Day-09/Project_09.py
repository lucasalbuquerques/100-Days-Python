import art
import os


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


print(art.logo)
print("Welcome to the secret auction program.")

auction = {}
next = True

while next == True:
    name = input("Whats your name? ")
    bid = int(input("What's your bid? "))
    auction[name] = bid

    continues = input("Are there any other bidders? Type 'yes' or 'no'".lower())
    if continues == "no":
        next = False
        clear()
    elif continues == "yes":
        next = True
        clear()
    else:
        print("I dont understand your option, so I will finish")
        next = False
        clear()


winner_bid = 0
for key in auction:
    if winner_bid < auction[key]:
        winner_bid = auction[key]
        pearson_winner = key
print(f"The winner is {pearson_winner} with a bid of ${winner_bid}")
input("Press enter to exit ;)")





