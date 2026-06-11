from collections import Counter

english_freq_order = "etaoinshrdlcumwfgypbvkjxqz"

def text_to_nums(text):
    return [c for c in text.lower() if c.isalpha()]

def decrypt_with_mapping(cipher, mapping):
    return ''.join(mapping.get(c, c) for c in cipher.lower())

def frequency_attack(cipher, topn=10):
    letters = text_to_nums(cipher)
    freq = Counter(letters)
    sorted_cipher_letters = [item[0] for item in freq.most_common()]
    results = []
    for i in range(topn):
        mapping = {}
        for j, c in enumerate(sorted_cipher_letters):
            if j < len(english_freq_order):
                mapping[c] = english_freq_order[(j+i) % 26]
        pt = decrypt_with_mapping(cipher, mapping)
        results.append(pt)
    return results

if __name__ == "__main__":
    cipher = "wklv lv d whvw phvvdjh"  # example ciphertext
    topn = 10
    candidates = frequency_attack(cipher, topn)
    for i, pt in enumerate(candidates, 1):
        print(f"Candidate {i}: {pt}")
