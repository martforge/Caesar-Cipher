# Write a function that implements a Caesar cipher to encrypt a given text. 
# The function should take two inputs: the text to be encrypted and the shift value. 
# It should handle both uppercase and lowercase letters, preserve spaces and punctuation, 
# and ensure the shift wraps correctly within the alphabet. Test your function with the input 'Hello, World' 
# and shift values of 3 and 13.

text = 'Hello, World'
shift = 3

not_encrypted = text
# print("not encrypted: ", not_encrypted)

def encryption(message, offset):
    encryptor = 'abcdefghijklmnopqrstuvwxyz'
    char_storage = ''

    for char in message.lower(): 
        if char == ' ' or char ==  ',' :
            char_storage += char
        else:
            index = encryptor.find(char)
            new_index = (index + offset) % len(encryptor)
            char_storage += encryptor[new_index]
    print(char_storage)

encryption(text, shift)