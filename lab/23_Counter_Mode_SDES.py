from Crypto.Cipher import DES
from Crypto.Util import Counter

key = b'\x0f\xfd\x0f\xfd\x0f\xfd\x0f\xfd'
ctr = Counter.new(64, initial_value=0)
plaintext = b'\x00\x01\x00\x02\x00\x04'

cipher = DES.new(key, DES.MODE_CTR, counter=ctr)
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

ctr = Counter.new(64, initial_value=0)
decipher = DES.new(key, DES.MODE_CTR, counter=ctr)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
