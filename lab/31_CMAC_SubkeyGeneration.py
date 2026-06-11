def left_shift_one_bit(block):
    shifted = int.from_bytes(block, 'big') << 1
    shifted &= (1 << (len(block)*8)) - 1
    return shifted.to_bytes(len(block), 'big')

def xor_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

def generate_subkeys(block_size_bits, L):
    if block_size_bits == 64:
        const = 0x1B
    elif block_size_bits == 128:
        const = 0x87
    else:
        raise ValueError("Unsupported block size")

    block_size = block_size_bits // 8
    L_bytes = L.to_bytes(block_size, 'big')

    K1 = left_shift_one_bit(L_bytes)
    if (L_bytes[0] & 0x80) != 0:
        K1 = xor_bytes(K1, (const).to_bytes(block_size, 'big'))

    K2 = left_shift_one_bit(K1)
    if (K1[0] & 0x80) != 0:
        K2 = xor_bytes(K2, (const).to_bytes(block_size, 'big'))

    return K1, K2

# Example: block size 128 bits, L = AES(0^128) simulated as integer
L = 0x1234567890ABCDEF1234567890ABCDEF
K1, K2 = generate_subkeys(128, L)
print("K1:", K1.hex())
print("K2:", K2.hex())
