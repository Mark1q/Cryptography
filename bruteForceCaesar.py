from caesar import caesar_cypher_decrypt

input_string = str(input("Please provide a string : "))

for i in range(1,25):
    print(f"Number of shifts : {i}",end=" ")
    caesar_cypher_decrypt(i,input_string)