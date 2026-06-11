def text_to_nums(t): return [ord(c)-97 for c in t if c.isalpha()]
def nums_to_text(n): return ''.join(chr(i+97) for i in n)

def encrypt(pt,key):
    n=text_to_nums(pt); c=[]
    for i in range(len(n)): c.append((n[i]+key[i])%26)
    return nums_to_text(c)

def decrypt(ct,key):
    n=text_to_nums(ct); p=[]
    for i in range(len(n)): p.append((n[i]-key[i])%26)
    return nums_to_text(p)

plaintext="sendmoremoney"
key=[9,0,1,7,23,15,21,14,11,11,2,8,9]
cipher=encrypt(plaintext,key)
print("Ciphertext:",cipher)

target="cashnotneeded"
cipher_nums=text_to_nums(cipher)
target_nums=text_to_nums(target)
new_key=[(cipher_nums[i]-target_nums[i])%26 for i in range(len(cipher_nums))]
print("New key:",new_key)
