import string

def affine_encrypt(text, a, b):
    result = []
    for ch in text.upper():
        if ch in string.ascii_uppercase:
            p = ord(ch) - 65
            c = (a * p + b) % 26
            result.append(chr(c + 65))
        else:
            result.append(ch)
    return "".join(result)

def affine_decrypt(cipher, a, b):
    # Check if 'a' is invertible mod 26
    def modinv(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None

    a_inv = modinv(a, 26)
    if a_inv is None:
        raise ValueError("Invalid 'a': not invertible mod 26")

    result = []
    for ch in cipher.upper():
        if ch in string.ascii_uppercase:
            c = ord(ch) - 65
            p = (a_inv * (c - b)) % 26
            result.append(chr(p + 65))
        else:
            result.append(ch)
    return "".join(result)

# Example usage
plaintext = "HELLO"
a, b = 5, 8   # 'a' must be coprime with 26
ciphertext = affine_encrypt(plaintext, a, b)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)

decrypted = affine_decrypt(ciphertext, a, b)
print("Decrypted:", decrypted)

# Demonstrate non one-to-one case
a_bad, b_bad = 2, 3
print("E([2,3],0) =", (a_bad*0+b_bad)%26)
print("E([2,3],13) =", (a_bad*13+b_bad)%26)
