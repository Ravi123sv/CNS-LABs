def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key = "".join([ch for ch in key.upper() if ch.isalpha()])
    j = 0
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            shift = ord(key[j % len(key)]) - ord('A')
            if mode == 'encrypt':
                result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            else:
                result += chr((ord(char) - ord(base) - shift) % 26 + ord(base))
            j += 1
        else:
            result += char
    return result

plaintext = input("Enter plaintext: ")
key = input("Enter key (letters only): ")

ciphertext = vigenere_cipher(plaintext, key, 'encrypt')
print("Ciphertext:", ciphertext)

decrypted = vigenere_cipher(ciphertext, key, 'decrypt')
print("Decrypted:", decrypted)
