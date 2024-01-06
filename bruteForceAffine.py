import math
from affine import affine_cypher_decrypt

input_string = str(input("Please provide a string : "))

for a in range(1,25):
    if math.gcd(a,26) == 1:
        for b in range(1,26):
            print(f"a = {a} and b = {b}",end=" ")
            affine_cypher_decrypt(a,b,26,input_string)

