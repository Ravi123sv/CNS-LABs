from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

key = DES3.adjust_key_parity(get_random_bytes(24))
iv = get_random_bytes(8)
cipher = DES3.new(key, DES3.MODE_CBC, iv)

plaintext = b"Secret Message 1234"
pad_len = 8 - (len(plaintext) % 8)
plaintext += bytes([pad_len]) * pad_len

ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES3.new(key, DES3.MODE_CBC, iv)
decrypted = decipher.decrypt(ciphertext)
unpadded = decrypted[:-decrypted[-1]]
print("Decrypted:", unpadded)
