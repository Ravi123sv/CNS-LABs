def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)

# Example: very large n (simulated with smaller for demo)
n = 3233   # pretend large modulus
e = 17
d = 2753

# Alice encodes letters A=0,...,Z=25
plaintext = "HELLO"
nums = [ord(ch)-65 for ch in plaintext]

ciphertext = [rsa_encrypt(m, e, n) for m in nums]
print("Ciphertext:", ciphertext)

decrypted_nums = [rsa_decrypt(c, d, n) for c in ciphertext]
decrypted_text = "".join(chr(m+65) for m in decrypted_nums)
print("Decrypted:", decrypted_text)

# Attack demonstration:
# Since plaintext space is only 26 values, attacker can brute-force all
possible_plaintexts = list(range(26))
lookup = {rsa_encrypt(m,e,n):m for m in possible_plaintexts}
recovered = [lookup[c] for c in ciphertext]
print("Attack recovers:", "".join(chr(m+65) for m in recovered))
