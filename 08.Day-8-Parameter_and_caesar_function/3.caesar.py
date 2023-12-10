alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_end = False
while not is_end:
    text = input("encrypt plain text")
    shift = int(input("number of shift"))
    direction = input("Type encode for encrypt decode for decrypt")

    def caesar(dire):
        def encrypt(text, shift):
            for char in text:
                if char in alphabet:
                    shift_index = alphabet.index(char)+shift
                    if shift_index >= 25:
                        shift_index = shift_index-26
                    print(alphabet[shift_index], end="")

        def decrypt(text, shift):
            for char in text:
                if char in alphabet:
                    shift_index = alphabet.index(char)-shift
                    if shift_index >= 25:
                        shift_index = shift_index-26
                    print(alphabet[shift_index], end="")

        if dire == "encode":
            encrypt(text, shift)
        if dire == "decode":
            decrypt(text, shift)
    caesar(dire=direction)
    end = input("\nDo you want to continue?Y,N")
    if end == "Y" or end == "y":
        is_end = True
