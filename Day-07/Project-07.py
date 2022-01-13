#Step 4

import random
import hangman_art
import hangman_words
from os import system, name

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)


def clear():
      
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
    
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()
    if guess not in chosen_word:
        lives = lives - 1
        print(f" You guessed {guess}, that's not in the word. You lose a life")
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])
        if lives <= 0:
            end_of_game = True
            print("You lose")
    else:   
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win.")
        