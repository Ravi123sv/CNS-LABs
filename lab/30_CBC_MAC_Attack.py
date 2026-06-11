def xor_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

def cbc_mac(key, message, block_size=16):
    # Simplified CBC-MAC: XOR with previous block, then "encrypt" by XOR with key
    prev = bytes([0]*block_size)
    for i in range(0, len(message), block_size):
        block = message[i:i+block_size]
        if len(block) < block_size:
            block = block + bytes([0]*(block_size-len(block)))
        prev = xor_bytes(xor_bytes(prev, block), key)
    return prev

# Example key and one-block message
key = b'\x01'*16
X = b'HELLOBLOCK12345'  # 16 bytes
T = cbc_mac(key, X)
print("MAC of X:", T)

# Forge two-block message: X || (X ⊕ T)
XxorT = xor_bytes(X, T)
two_block = X + XxorT
T2 = cbc_mac(key, two_block)
print("MAC of X||(X⊕T):", T2)
