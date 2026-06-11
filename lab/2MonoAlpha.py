def monoalphabetic_cipher(text, key_map):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            idx = ord(char.upper()) - ord('A')
            mapped = key_map[idx]
            result += mapped.upper() if char.isupper() else mapped.lower()
        else:
            result += char
    return result

key_map = list("QWERTYUIOPASDFGHJKLZXCVBNM")  # substitution alphabet
plaintext = input("Enter plaintext: ")
ciphertext = monoalphabetic_cipher(plaintext, key_map)
print("Ciphertext:", ciphertext)
