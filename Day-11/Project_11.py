from art import logo
import random


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def soma_cards(cards):
    soma = 0
    for id in cards:
        soma = soma + id
    return soma

def print_cards(player, dealer):
    print(f"Your cards: {player}")
    print(f"Computer's first card: {dealer[0]}")


def print_cards_final(player, dealer):
    print(f"Your cards: {player}")
    print(f"Computer's first card: {dealer}")

play_again = "y"

while play_again == "y":
    print(logo)
    player = []
    dealer = []
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))
    print_cards(player,dealer)
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while another_card == "y":
        player.append(random.choice(cards))
        if soma_cards(player) < 21:
            print_cards(player, dealer)
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            another_card = "n"

    if soma_cards(player) > 21:
        print_cards_final(player, dealer)
        print("You lost")

    elif soma_cards(player) > soma_cards(dealer) and soma_cards(dealer) < 12:
        dealer.append(random.choice(cards))
        if soma_cards(dealer) > 21:
            print_cards_final(player, dealer)
            print("You Win")
        elif soma_cards(player) > soma_cards(dealer):
            print_cards_final(player, dealer)
            print("You Win")
        elif soma_cards(player) < soma_cards(dealer):
            print_cards_final(player, dealer)
            print("You Lost")
        elif soma_cards(player) == soma_cards(dealer):
            print_cards_final(player, dealer)
            print("Draw")
    elif soma_cards(player) > soma_cards(dealer):
        print_cards_final(player, dealer)
        print("You Win")
    elif soma_cards(player) < soma_cards(dealer):
        print_cards_final(player, dealer)
        print("You Lost")
    elif soma_cards(player) == soma_cards(dealer):
        print_cards_final(player, dealer)
        print("Draw")

    play_again = input("Do you want to play a game of Blackjack ? Type 'y' or 'n'").lower()














