import string

def input_output():
    operation = str(input("Would you like to encrypt or decrypt a string : "))

    if operation != "encrypt" and operation != "decrypt":
        print("Input should be 'encrypt' or 'decrypt' ")
        return

    input_string = str(input("Please provide a string : "))
    input_shifts = int(input("Number of shifts : "))

    if operation == "encrypt":
        caesar_cypher_encrypt(input_shifts,input_string)
    else:
        caesar_cypher_decrypt(input_shifts,input_string)

def caesar_cypher_encrypt(shift,str):
    result_string = ""

    if shift % 26 == 0:
        print(str)
        return

    if shift < 0:
        shift = shift % 26 + 26
    
    alphabet = list(string.ascii_lowercase)
    dictionary = {}
    i = 0

    for letter in alphabet:
        dictionary[letter] = i
        i = i + 1
    
    for char in str:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
                pos = dictionary[char] + shift
                while pos > 26:
                    pos = pos - 26
                result_string += alphabet[pos].upper()
            else:
                pos = dictionary[char] + shift
                while pos > 26:
                    pos = pos - 26
                result_string += alphabet[pos]
        else:
            pos = dictionary[char] + shift
            while pos > 26:
                pos = pos - 26
            result_string += char

    print(result_string)

def caesar_cypher_decrypt(shift,str):
    result_string = ""

    if shift % 26 == 0:
        print(str)
        return

    if shift < 0:
        shift = shift % 26 + 26
    
    alphabet = list(string.ascii_lowercase)
    dictionary = {}
    i = 0

    for letter in alphabet:
        dictionary[letter] = i
        i = i + 1
    
    for char in str:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
                pos = dictionary[char] - shift
                while pos < 0:
                    pos = pos + 26
                result_string += alphabet[pos].upper()
            else:
                pos = dictionary[char] - shift
                while pos < 0:
                    pos = pos + 26
                result_string += alphabet[pos]
        else:
            result_string += char

    print(result_string)

if __name__ == '__main__':
    input_output()