import string
from collections import Counter

# English letter frequency (approximate order of likelihood)
english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_attack(ciphertext, top_n=10):
    # Count frequency of letters in ciphertext
    counts = Counter([ch for ch in ciphertext.upper() if ch in string.ascii_uppercase])
    # Sort letters by frequency in ciphertext
    cipher_freq_order = "".join([item[0] for item in counts.most_common()])

    # Generate possible plaintexts by mapping most frequent ciphertext letters
    # to most frequent English letters
    results = []
    for shift in range(top_n):
        mapping = {}
        for i, ch in enumerate(cipher_freq_order):
            if i < len(english_freq_order):
                mapping[ch] = english_freq_order[(i+shift) % len(english_freq_order)]
        # Apply mapping
        plaintext = "".join([mapping.get(ch, ch) for ch in ciphertext.upper()])
        results.append(plaintext)
    return results

# Example ciphertext (monoalphabetic substitution)
ciphertext = "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"

print("Ciphertext:", ciphertext)
possible_plaintexts = frequency_attack(ciphertext, top_n=10)
for i, pt in enumerate(possible_plaintexts, 1):
    print(f"Plaintext guess {i}:", pt)
