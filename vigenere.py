def vigenere_cipher(text, key, mode):
    result = ''
    key_length = len(key)
    key_as_int = [ord(k) for k in key]

    key_index = 0  # Initialize index for the key

    for i in range(len(text)):
        if text[i].isalpha():
            key_shift = key_as_int[key_index]
            if mode == 'encrypt':
                result += chr((ord(text[i]) + key_shift) % 26 + ord('A'))
            elif mode == 'decrypt':
                result += chr((ord(text[i]) - key_shift) % 26 + ord('A'))
            key_index = (key_index + 1) % key_length  # Update index for the key
        else:
            result += text[i]

    return result

def main():
    mode = input("Enter 'encrypt' or 'decrypt': ").lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return

    message = input("Enter the message: ").upper()
    key = input("Enter the key: ").upper()

    result = vigenere_cipher(message, key, mode)
    print(f"{mode.capitalize()}ed message: {result}")

if __name__ == "__main__":
    main()
