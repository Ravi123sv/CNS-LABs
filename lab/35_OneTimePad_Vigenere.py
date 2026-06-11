import random
import string

def generate_key(length):
    # Key is a stream of random numbers between 0 and 26
    return [random.randint(0,26) for _ in range(length)]

def encrypt(plaintext, key):
    ciphertext = []
    for i, ch in enumerate(plaintext.upper()):
        if ch in string.ascii_uppercase:
            shift = key[i]
            val = (ord(ch) - 65 + shift) % 26
            ciphertext.append(chr(val + 65))
        else:
            ciphertext.append(ch)
    return "".join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    for i, ch in enumerate(ciphertext.upper()):
        if ch in string.ascii_uppercase:
            shift = key[i]
            val = (ord(ch) - 65 - shift) % 26
            plaintext.append(chr(val + 65))
        else:
            plaintext.append(ch)
    return "".join(plaintext)

# Example usage
plaintext = "HELLO"
key = generate_key(len(plaintext))
print("Plaintext:", plaintext)
print("Key:", key)

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted = decrypt(ciphertext, key)
print("Decrypted:", decrypted)
