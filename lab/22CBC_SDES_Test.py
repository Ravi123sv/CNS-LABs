from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'\x0f\xfd\x0f\xfd\x0f\xfd\x0f\xfd'  # 8-byte key
iv = b'\xaa'*8
plaintext = b'\x00\x01\x02\x03'

cipher = DES.new(key, DES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext,8))
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext),8)
print("Decrypted:", decrypted)
