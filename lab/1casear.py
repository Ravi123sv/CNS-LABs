def caesar_cipher(text, k, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + k) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - k) % 26 + base)
        else:
            result += char
    return result

plaintext = input("Enter plaintext: ")
key = int(input("Enter key (1-25): "))

ciphertext = caesar_cipher(plaintext, key, mode='encrypt')
print("Ciphertext:", ciphertext)

decrypted = caesar_cipher(ciphertext, key, mode='decrypt')
print("Decrypted text:", decrypted)