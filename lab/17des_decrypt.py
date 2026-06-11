SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2,
                  1, 2, 2, 2, 2, 2, 2, 1]
def left_shift(bits, n):
    return bits[n:] + bits[:n]
def generate_round_keys(key56):
    C = key56[:28]
    D = key56[28:]
    round_keys = []
    for shift in SHIFT_SCHEDULE:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        round_keys.append(C + D)  
    return round_keys
def feistel(right, subkey):
    return ''.join(str((int(r)^int(k))%2) for r,k in zip(right, subkey[:len(right)]))
def des_decrypt(ciphertext64, round_keys):
    L = ciphertext64[:32]
    R = ciphertext64[32:]
    for subkey in reversed(round_keys):
        newR = ''.join(str((int(l)^int(f))%2) for l,f in zip(L, feistel(R, subkey)))
        L, R = R, newR
    return L + R
if __name__ == "__main__":
    key56 = "0001001100110100010101110111100110011011101111001101111111110001"
    round_keys = generate_round_keys(key56)
    ciphertext64 = "1111000010101010111100001010101011110000101010101111000010101010"
    plaintext64 = des_decrypt(ciphertext64, round_keys)
    print("Ciphertext:", ciphertext64)
    print("Plaintext (decrypted):", plaintext64)
