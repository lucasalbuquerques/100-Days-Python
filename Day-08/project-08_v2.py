import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def call_the_caesar(text, shift, direction):
    if direction == "encode":
        text_encrypt = ""
        for letter in text:
            position = alphabet.index(letter) + shift
            while position > 25:
                position = position - 26
            text_encrypt = (str(text_encrypt) + str(alphabet[position]))
        print(text_encrypt)
    elif direction == "decode":
        text_decrypt = ""
        for letter in text:
            position = alphabet.index(letter) - shift
            while position < 0:
                position = position + 26
            text_decrypt = (str(text_decrypt) + str(alphabet[position]))
        print(text_decrypt)
    else:
        print("Opção invalida")

again = True

while again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    call_the_caesar(text=text, shift=shift, direction=direction)
    message = input("Type 'yes' if you want to go again. Otherwise type 'no'. ".lower())
    if message == "yes":
        again = True
    elif message == "no":
        print("I will close the software, have a nice day !")
        again = False
    else:
        print("I don't understand your option, I will close the software, bye")
        again = False


