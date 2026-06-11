from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

k=get_random_bytes(16)
d=b'ABCDEFGHIJKLMNOP'

e=AES.new(k,AES.MODE_ECB)
c=e.encrypt(d)
print("ECB decrypt:",e.decrypt(c))

iv=get_random_bytes(16)
c=AES.new(k,AES.MODE_CBC,iv).encrypt(d)
print("CBC decrypt:",AES.new(k,AES.MODE_CBC,iv).decrypt(c))

# simulate error in C1 for CBC
c_err=bytearray(c);c_err[0]^=1
print("CBC with error:",AES.new(k,AES.MODE_CBC,iv).decrypt(bytes(c_err)))
