# Cryptography

Cryptography concepts and cyphers implemented into Python

[Source](https://picoctf.org/learning_guides/Book-2-Cryptography.pdf)

## Caesar Cipher

The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of positions up or down the alphabet. It is named after Julius Caesar, who is historically credited with its use.

- **Key Parameter**: The key for the Caesar cipher is the number of positions each letter is shifted.

## Affine Cipher

The Affine cipher is a type of monoalphabetic substitution cipher that involves a mathematical function to encrypt and decrypt. It uses the formula `E(x) = (ax + b) % m`, where `x` is the position of the letter in the alphabet, `a` and `b` are the key parameters, and `m` is the size of the alphabet.

- **Key Parameters**: The two key parameters `a` and `b` must be chosen carefully to ensure the encryption and decryption are reversible.

## Vigenere Cipher

The Vigenere cipher is a polyalphabetic substitution cipher that uses a keyword to shift letters in the plaintext. It is more complex than the Caesar cipher and provides a higher level of security.

- **Key Parameter**: The key for the Vigenere cipher is a keyword, which is repeated to match the length of the plaintext.

## Hill Cipher _(without source code yet)_

The Hill cipher is a polygraphic substitution cipher based on linear algebra. It encrypts blocks of plaintext at a time using an invertible matrix. The size of the matrix depends on the block size chosen.

- **Key Parameter**: The key for the Hill cipher is a matrix. The matrix must be invertible for both encryption and decryption to be possible.


Certainly! A README file typically doesn't support embedded images, but I can guide you on how to structure the README and where you can add images. You can include links to hosted images, and users can follow those links to view the images.

Let's create a README for the Diffie-Hellman key exchange:

---

## Diffie-Hellman Key Exchange

The Diffie-Hellman key exchange is a method for two parties to securely agree on a shared secret over an insecure communication channel. It is a fundamental building block in modern cryptography.

## Overview

The Diffie-Hellman key exchange was introduced by Whitfield Diffie and Martin Hellman in 1976. It enables two parties to agree on a shared secret over an untrusted network without directly exchanging the secret.

## Key Exchange Process

### Step 1: Setup

Two parties, Alice and Bob, agree on public parameters:
- A large prime number `p`
- A primitive root modulo `p`, denoted as `g`

These parameters are public and can be freely shared.

### Step 2: Private Keys

Both Alice and Bob generate their private keys:
- Alice selects a private key `a`
- Bob selects a private key `b`

These private keys are kept secret.

### Step 3: Public Keys

Both Alice and Bob compute their public keys using the formula:
```
A = g^a mod p      # Alice's public key
B = g^b mod p      # Bob's public key
```

### Step 4: Exchange

Alice and Bob exchange their public keys (`A` and `B`) over the insecure channel.

### Step 5: Shared Secret

Both Alice and Bob compute the shared secret using the received public key and their own private key:
```
shared_secret_Alice = B^a mod p
shared_secret_Bob = A^b mod p
```

The shared secret is the same for both parties.

## Understanding the Algorithm

The security of Diffie-Hellman relies on the difficulty of the discrete logarithm problem. An eavesdropper would need to compute the private keys from the public keys, which is computationally infeasible when using large prime numbers.

## Security Considerations

While Diffie-Hellman provides secure key exchange, it is vulnerable to man-in-the-middle attacks. To mitigate this, the exchanged public keys are often authenticated.
