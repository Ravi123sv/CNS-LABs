import string
from collections import Counter

def additive_decrypt(ciphertext, shift):
    result = []
    for ch in ciphertext.upper():
        if ch in string.ascii_uppercase:
            val = (ord(ch)-65 - shift) % 26
            result.append(chr(val+65))
        else:
            result.append(ch)
    return "".join(result)

def frequency_attack(ciphertext, top_n=10):
    counts = Counter([ch for ch in ciphertext.upper() if ch in string.ascii_uppercase])
    most_common = counts.most_common(1)[0][0]
    # Assume most common letter in ciphertext corresponds to 'E'
    shift_guess = (ord(most_common)-65) - (ord('E')-65)
    results = []
    for delta in range(top_n):
        shift = (shift_guess+delta) % 26
        results.append(additive_decrypt(ciphertext, shift))
    return results

ciphertext = "ZHOFRPH WR WKH FLSKHU"
print("Ciphertext:", ciphertext)
for i, guess in enumerate(frequency_attack(ciphertext, top_n=10),1):
    print(f"Guess {i}:", guess)
