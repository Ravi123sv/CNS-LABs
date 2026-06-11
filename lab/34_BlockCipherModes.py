from Crypto.Cipher import AES

def pad_message(msg, block_size=16):
    # Padding: 1 bit (0x80) followed by zeros
    pad_len = block_size - (len(msg) % block_size)
    return msg + b'\x80' + b'\x00'*(pad_len-1)

key = b'1234567890123456'
iv = b'1234567890123456'
plaintext = b"HELLO WORLD"
padded = pad_message(plaintext)

# ECB mode
cipher_ecb = AES.new(key, AES.MODE_ECB)
ct_ecb = cipher_ecb.encrypt(padded)
print("ECB ciphertext:", ct_ecb)

# CBC mode
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
ct_cbc = cipher_cbc.encrypt(padded)
print("CBC ciphertext:", ct_cbc)

# CFB mode
cipher_cfb = AES.new(key, AES.MODE_CFB, iv)
ct_cfb = cipher_cfb.encrypt(padded)
print("CFB ciphertext:", ct_cfb)
