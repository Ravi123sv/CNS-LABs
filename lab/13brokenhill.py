def mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def text_to_nums(text):
    return [ord(c) - 97 for c in text if c != ' ']

def nums_to_text(nums):
    return ''.join(chr(n + 97) for n in nums)

def encrypt(nums, key):
    ct = []
    for i in range(0, len(nums), 2):
        p1, p2 = nums[i], nums[i+1]
        c1 = (key[0][0]*p1 + key[0][1]*p2) % 26
        c2 = (key[1][0]*p1 + key[1][1]*p2) % 26
        ct += [c1, c2]
    return ct

def recover_key(plain, cipher):
    det = (plain[0]*plain[3] - plain[1]*plain[2]) % 26
    det_inv = mod_inv(det, 26)
    if det_inv is None:
        raise ValueError("Plaintext matrix not invertible mod 26")
    adj = [[plain[3], -plain[1]], [-plain[2], plain[0]]]
    invP = [[(det_inv*adj[0][0])%26, (det_inv*adj[0][1])%26],
            [(det_inv*adj[1][0])%26, (det_inv*adj[1][1])%26]]
    key = [[(cipher[0]*invP[0][0] + cipher[2]*invP[0][1]) % 26,
            (cipher[0]*invP[1][0] + cipher[2]*invP[1][1]) % 26],
           [(cipher[1]*invP[0][0] + cipher[3]*invP[0][1]) % 26,
            (cipher[1]*invP[1][0] + cipher[3]*invP[1][1]) % 26]]
    return key

# Demo with invertible plaintext pairs
key = [[9,4],[5,7]]
plaintexts = ["ba","ab"]   # identity matrix, invertible
plain_nums, cipher_nums = [], []
for pt in plaintexts:
    nums = text_to_nums(pt)
    plain_nums += nums
    cipher_nums += encrypt(nums, key)

print("Plaintext samples:", plaintexts)
print("Ciphertext samples:", [nums_to_text(encrypt(text_to_nums(pt), key)) for pt in plaintexts])

recovered = recover_key(plain_nums[:4], cipher_nums[:4])
print("Recovered key matrix:")
for row in recovered:
    print(row)
