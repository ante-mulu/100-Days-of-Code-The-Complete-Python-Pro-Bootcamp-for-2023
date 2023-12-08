alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift):
    encrypted_message = []
    for char in plain_text:
        encrypted_char = ord(char)+shift
        encrypted_message.append(encrypted_char)
    for char in encrypted_message:
        print(chr(char), end="")


def decode(cipher_text, shfit):
    decrypted_message = []
    for char in cipher_text:
        decipher_char = ord(char)-shift
        decrypted_message.append(decipher_char)
    for char in decrypted_message:
        print(chr(char), end="")


the_end = False
while not the_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    if direction == "decode":
        decode(text, shift)
    end = input("\nDo you want to continue:yes,no:  ")
    if end == "no":
        the_end = True


# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
