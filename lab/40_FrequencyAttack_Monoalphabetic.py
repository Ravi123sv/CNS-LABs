import string
from collections import Counter

english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_attack(ciphertext, top_n=10):
    counts = Counter([ch for ch in ciphertext.upper() if ch in string.ascii_uppercase])
    cipher_freq_order = "".join([item[0] for item in counts.most_common()])
    results = []
    for shift in range(top_n):
        mapping = {}
        for i, ch in enumerate(cipher_freq_order):
            if i < len(english_freq_order):
                mapping[ch] = english_freq_order[(i+shift)%len(english_freq_order)]
        plaintext = "".join([mapping.get(ch,ch) for ch in ciphertext.upper()])
        results.append(plaintext)
    return results

ciphertext = "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"
print("Ciphertext:", ciphertext)
for i, guess in enumerate(frequency_attack(ciphertext, top_n=10),1):
    print(f"Guess {i}:", guess)
