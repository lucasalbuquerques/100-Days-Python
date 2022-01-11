import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for id in chosen_word:
    display.append("_")

end_of_game = False

while not end_of_game:
    print(f'Pssst, the solution is {chosen_word}.')
    guess = input("Guess a letter: ").lower()
    for id in range(0, len(chosen_word)):
        if chosen_word[id] == guess:
            display[id] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
        



        
