import math

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Invalid 'a'. Must be coprime with 26.")
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr(((a * (ord(char) - ord(base)) + b) % 26) + ord(base))
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Invalid 'a'. Must be coprime with 26.")
    a_inv = mod_inverse(a, 26)
    result = ""
    for char in cipher:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr(((a_inv * ((ord(char) - ord(base)) - b)) % 26) + ord(base))
        else:
            result += char
    return result

print("Valid values of 'a' are: {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}")
plaintext = input("Enter plaintext: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

ciphertext = affine_encrypt(plaintext, a, b)
print("Ciphertext:", ciphertext)

decrypted = affine_decrypt(ciphertext, a, b)
print("Decrypted:", ciphertext)
