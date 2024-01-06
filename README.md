# Cryptography

Cryptography concepts and cyphers implemented into Python

[Source](https://picoctf.org/learning_guides/Book-2-Cryptography.pdf)

## Table of Contents

1. [Caesar Cipher](#caesar-cipher)
2. [Affine Cipher](#affine-cipher)
3. [Vigenere Cipher](#vigenere-cipher)
4. [Hill Cipher](#hill-cipher)
5. [Usage](#usage)
6. [Installation](#installation)
7. [Contributing](#contributing)
8. [License](#license)

## Caesar Cipher

The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of positions up or down the alphabet. It is named after Julius Caesar, who is historically credited with its use.

- **Key Parameter**: The key for the Caesar cipher is the number of positions each letter is shifted.

## Affine Cipher

The Affine cipher is a type of monoalphabetic substitution cipher that involves a mathematical function to encrypt and decrypt. It uses the formula `E(x) = (ax + b) % m`, where `x` is the position of the letter in the alphabet, `a` and `b` are the key parameters, and `m` is the size of the alphabet.

- **Key Parameters**: The two key parameters `a` and `b` must be chosen carefully to ensure the encryption and decryption are reversible.

## Vigenere Cipher

The Vigenere cipher is a polyalphabetic substitution cipher that uses a keyword to shift letters in the plaintext. It is more complex than the Caesar cipher and provides a higher level of security.

- **Key Parameter**: The key for the Vigenere cipher is a keyword, which is repeated to match the length of the plaintext.

## Hill Cipher

The Hill cipher is a polygraphic substitution cipher based on linear algebra. It encrypts blocks of plaintext at a time using an invertible matrix. The size of the matrix depends on the block size chosen.

- **Key Parameter**: The key for the Hill cipher is a matrix. The matrix must be invertible for both encryption and decryption to be possible.

## Usage

Detailed usage examples for each cipher are provided in their respective sections above.

## Installation

Install the library using pip:

```bash
pip install classic-ciphers
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
