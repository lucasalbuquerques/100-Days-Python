import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for id in chosen_word:
    display.append("_")

display_with_word = []
for id in chosen_word:
    display_with_word.append(id)

while display_with_word != display:
    print(f'Pssst, the solution is {chosen_word}.')
    guess = input("Guess a letter: ").lower()
    for id in range(0, len(chosen_word)):
        if chosen_word[id] == guess:
            display[id] = guess
    print(display)
print("You win")



        
