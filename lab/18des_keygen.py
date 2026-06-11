SHIFT_SCHEDULE = [1,1,2,2,2,2,2,2,
                  1,2,2,2,2,2,2,1]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_subkeys(key56):
    C = key56[:28]
    D = key56[28:]
    subkeys = []
    for shift in SHIFT_SCHEDULE:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        # take first 24 bits from C and first 24 bits from D
        subkey = C[:24] + D[:24]
        subkeys.append(subkey)
    return subkeys

if __name__ == "__main__":
    # Example 56-bit key as string of bits
    key56 = "00010011001101000101011101111001100110111011110011011111111100"
    subkeys = generate_subkeys(key56)
    for i, sk in enumerate(subkeys,1):
        print(f"Round {i:2d} subkey: {sk}")
