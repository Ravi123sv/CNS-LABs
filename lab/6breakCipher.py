def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        return None  # No modular inverse if gcd ≠ 1
    else:
        return x % m

def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"Invalid 'a'={a}. No modular inverse exists modulo 26.")
    result = ""
    for char in cipher:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr(((a_inv * ((ord(char) - ord(base)) - b)) % 26) + ord(base))
        else:
            result += char
    return result

# Example usage
a, b = 3, 15
ciphertext = input("Enter ciphertext: ")
plaintext = affine_decrypt(ciphertext.strip(), a, b)
print("Decrypted plaintext:", plaintext)