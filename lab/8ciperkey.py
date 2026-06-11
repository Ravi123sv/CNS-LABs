def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()
    seen = set()
    cipher_alphabet = []
    for char in keyword:
        if char.isalpha() and char not in seen:
            cipher_alphabet.append(char)
            seen.add(char)
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in seen:
            cipher_alphabet.append(char)
    return cipher_alphabet

def monoalphabetic_encrypt(plaintext, cipher_alphabet):
    plaintext = plaintext.upper()
    result = ""
    for char in plaintext:
        if char.isalpha():
            index = ord(char) - ord('A')
            result += cipher_alphabet[index]
        else:
            result += char
    return result

def monoalphabetic_decrypt(ciphertext, cipher_alphabet):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            index = cipher_alphabet.index(char)
            result += chr(index + ord('A'))
        else:
            result += char
    return result

keyword = "CIPHER"
cipher_alphabet = generate_cipher_alphabet(keyword)
print("Cipher alphabet:", "".join(cipher_alphabet))

plaintext = input("Enter plaintext: ")
ciphertext = monoalphabetic_encrypt(plaintext, cipher_alphabet)
print("Ciphertext:", ciphertext)

decrypted = monoalphabetic_decrypt(ciphertext, cipher_alphabet)
print("Decrypted:", decrypted)
