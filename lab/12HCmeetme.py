def mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def text_to_nums(text):
    return [ord(c) - 97 for c in text if c != ' ']

def nums_to_text(nums):
    return ''.join(chr(n + 97) for n in nums)

def encrypt(pt, key):
    nums = text_to_nums(pt)
    if len(nums) % 2: nums.append(25)
    ct = []
    for i in range(0, len(nums), 2):
        p1, p2 = nums[i], nums[i+1]
        c1 = (key[0][0]*p1 + key[0][1]*p2) % 26
        c2 = (key[1][0]*p1 + key[1][1]*p2) % 26
        ct += [c1, c2]
    return nums_to_text(ct)

def decrypt(ct, key):
    det = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26
    det_inv = mod_inv(det, 26)
    adj = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]
    inv = [[(det_inv*adj[0][0])%26, (det_inv*adj[0][1])%26],
           [(det_inv*adj[1][0])%26, (det_inv*adj[1][1])%26]]
    nums = text_to_nums(ct)
    pt = []
    for i in range(0, len(nums), 2):
        c1, c2 = nums[i], nums[i+1]
        p1 = (inv[0][0]*c1 + inv[0][1]*c2) % 26
        p2 = (inv[1][0]*c1 + inv[1][1]*c2) % 26
        pt += [p1, p2]
    return nums_to_text(pt)

key = [[9,4],[5,7]]
plaintext = "meet me at the usual place at ten rather than eight oclock"
cipher = encrypt(plaintext, key)
print("Ciphertext:", cipher)
print("Decrypted:", decrypt(cipher, key))
