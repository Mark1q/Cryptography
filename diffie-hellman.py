import random

class Person:
    def __init__(self,public_key,private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.combination_key = (public_key[1] ** private_key) % public_key[0]

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_primitive_root(g, p):
    powers = set()
    for i in range(1, p):
        powers.add(pow(g, i, p))
    return len(powers) == p - 1

def primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

def red(str):
    return "\033[31m" + str + "\033[0m"

def blue(str):
    return "\033[34m" + str + "\033[0m"

def bold(str):
    return "\033[1m" + str + '\033[0m'


primes = [i for i in range(0,1000) if isPrime(i)]

#
#
#

p = random.choice(primes)
g = primitive_root(p)


while g == None:
    p = random.choice(primes)
    g = primitive_root(p)

Alice = Person([p,g],random.randint(1,10)) 
Bob = Person([p,g],random.randint(1,10)) 

while Alice.private_key == Bob.private_key:
    Bob = Person([p,g],random.randint(1,10))



print(f"\n{red("Red")} is private")
print(f"{blue("Blue")} is public\n")
print("==== FIRST STEP === \n")
print(f"{bold("• Choose a public key that they both agree upon")}")
print(f"\nPublic key = {blue(f"{p,g}")}")
print(f"\n{bold("• Choose personal private keys")}\n")
print(f"Alice's private key = {red(f"{Alice.private_key}")}")
print(f"Bob's private key = {red(f"{Bob.private_key}")}\n")
print("==== SECOND STEP ===\n")
print(f"{bold("• Combine the public key with the private key using this formula")} : {blue("generator(g)")} ^ {red("private_key")}(mod {blue("p")})\n")
print(f"A = {blue(f"{Alice.public_key[1]}")}^{red(f"{Alice.private_key}")}(mod {blue(f"{Alice.public_key[0]}")}) = {blue(f"{Alice.combination_key}")}")
print(f"B = {blue(f"{Bob.public_key[1]}")}^{red(f"{Bob.private_key}")}(mod {blue(f"{Bob.public_key[0]}")}) = {blue(f"{Bob.combination_key}")}")
print("\n=== FINAL STEP ===\n")
print(f"{bold(f"• They exchange the values and combine the keys(")}{blue("A")} {bold("and")} {blue("B")}{bold(") with their respective private keys")}\n")
print(f"Alice's key = {blue(f"{Bob.combination_key}")}^{red(f"{Alice.private_key}")}(mod {blue(f"{Alice.public_key[0]}")}) = {red(f"{(Bob.combination_key ** Alice.private_key) % Alice.public_key[0]}")}")
print(f"Bob's key = {blue(f"{Alice.combination_key}")}^{red(f"{Bob.private_key}")}(mod {blue(f"{Bob.public_key[0]}")}) = {red(f"{(Alice.combination_key ** Bob.private_key) % Bob.public_key[0]}")}")
print("\nAnd now they have the same secret key !!!")