import math
import string

def input_output():
    operation = str(input("Would you like to encrypt or decrypt a string : "))

    if operation != "encrypt" and operation != "decrypt":
        print("Input should be 'encrypt' or 'decrypt' ")
        return

    input_string = str(input("Please provide a string : "))
    input_a = int(input("Value of a : "))
    input_b = int(input("Value of b : "))
    input_m = int(input("Value of m(alphabet size) : "))

    if operation == "encrypt":
        affine_cypher_encrypt(input_a,input_b,input_m,input_string)
    else:
        affine_cypher_decrypt(input_a,input_b,input_m,input_string)

def dictionary_alphabet_generator():
    alphabet = list(string.ascii_lowercase)
    dictionary = {}
    i = 0

    for letter in alphabet:
        dictionary[letter] = i
        i = i + 1
    
    return dictionary

def affine_cypher_encrypt(a,b,m,str):
    result_string = ""

    if math.gcd(a,m) != 1:
       print(f"{a} and {m} should be coprime")
       return

    a = a % m
    b = b % m
    
    dict = dictionary_alphabet_generator()
    
    for character in str:
        if character.isalpha():
            value = (dict[character] * a + b) % m

            for key,val in dict.items():
                if val == value:
                    if(character.islower()):
                        result_string += key.lower()
                    else:
                        result_string += key.upper()
        else :
            result_string += character

    print(f"Encrypted string : {result_string}")

def affine_cypher_decrypt(a,b,m,str):
    result_string = ""

    if math.gcd(a,m) != 1:
       print(f"{a} and {m} should be coprime")
       return
    
    a = a % m
    b = b % m
    
    dict = dictionary_alphabet_generator()

    inverse_a = 0
    
    for i in range(25):
        if((a * i) % m == 1):
            inverse_a = i
            break
    
    for character in str:
        if character.isalpha():
            val = (inverse_a * (dict[character] - b)) % m

            for key,value in dict.items():
                if value == val:
                    if character.islower():
                        result_string += key.lower()
                    else:
                        result_string += key.upper()
        
        else: 
            result_string += character

    print(f"Decrypted string : {result_string}")


if __name__ == '__main__':
    input_output()


