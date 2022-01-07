import random

player = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
options_name = ["Rock" , "Paper", "Scissors"]


print(f"Player chose: {options_name[player]}")
print(options[player])
print()
print(f"Computer chose: {options_name[computer]}")
print(options[computer])



if player == computer:
    print("It's a draw!")
elif player == 0 and computer == 1:
    print("You lose!")
    
elif player == 0 and computer == 2:
    print("You win!")
elif player == 1 and computer == 0:
    print("You win!")
    
elif player == 1 and computer == 2:
    print("You lose!")
    
elif player == 2 and computer == 0:
    print("You lose!")
elif player == 2 and computer == 1:
    print("You win!")

