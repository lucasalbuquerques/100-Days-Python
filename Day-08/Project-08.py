alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    text_encrypt = ""
    for letter in text:
        position = alphabet.index(letter) + shift
        while position > 25:
            position = position - 26
        text_encrypt = (str(text_encrypt) + str(alphabet[position]))
    print(text_encrypt)


def decrypt(text, shift):
    text_decrypt = ""
    for letter in text:
        position = alphabet.index(letter) - shift
        while position < 0:
            position = position + 26
        text_decrypt = (str(text_decrypt) + str(alphabet[position]))
    print(text_decrypt)


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Opção invalida")
