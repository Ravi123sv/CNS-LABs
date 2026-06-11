from Crypto.Cipher import AES

def pad(data, block_size):
    pad_len = block_size - (len(data) % block_size)
    return data + b'\x80' + b'\x00'*(pad_len-1)

key = b'1234567890123456'
iv = b'1234567890123456'
data = pad(b"HELLO WORLD",16)

cipher_ecb = AES.new(key,AES.MODE_ECB)
cipher_cbc = AES.new(key,AES.MODE_CBC,iv)
cipher_cfb = AES.new(key,AES.MODE_CFB,iv)

print(cipher_ecb.encrypt(data))
print(cipher_cbc.encrypt(data))
print(cipher_cfb.encrypt(data))
