import numpy as np

def hill_encrypt(plaintext, key_matrix):
    vec = np.array([ord(ch)-65 for ch in plaintext.upper()])
    ct_vec = np.dot(key_matrix, vec) % 26
    return "".join(chr(int(x)+65) for x in ct_vec)

# Example 2x2 Hill cipher
key = np.array([[3,3],[2,5]])
plaintext = "HI"
ciphertext = hill_encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)

# Known plaintext attack: given enough (plaintext,ciphertext) pairs,
# attacker can set up linear equations and solve for key matrix.
