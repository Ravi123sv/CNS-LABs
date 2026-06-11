from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Key must be 8 bytes (DES uses 56 bits + parity bits)
key = b'12345678'
cipher = DES.new(key, DES.MODE_ECB)

# Plaintext: 64 bits (8 bytes)
plaintext = b'ABCDEFGH'
print("Plaintext:", plaintext)

# Encrypt
ciphertext = cipher.encrypt(pad(plaintext, 8))
print("Ciphertext:", ciphertext)

# Decrypt
decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), 8)
print("Decrypted:", decrypted)
