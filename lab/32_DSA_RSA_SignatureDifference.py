import random
import hashlib

# Simplified DSA-like signature demonstration
def dsa_sign(message, p, q, g, x):
    H = int(hashlib.sha1(message.encode()).hexdigest(),16) % q
    k = random.randint(1,q-1)
    r = pow(g,k,p) % q
    s = (pow(k,-1,q) * (H + x*r)) % q
    return (r,s)

# Simplified RSA-like signature demonstration
def rsa_sign(message, n, d):
    H = int(hashlib.sha1(message.encode()).hexdigest(),16)
    return pow(H,d,n)

# Parameters for DSA demo
p = 23
q = 11
g = 4
x = 3

msg = "HELLO"

# Two DSA signatures of same message
sig1 = dsa_sign(msg,p,q,g,x)
sig2 = dsa_sign(msg,p,q,g,x)
print("DSA signatures differ:", sig1, sig2)

# RSA demo
n = 3233
d = 2753
sig_rsa1 = rsa_sign(msg,n,d)
sig_rsa2 = rsa_sign(msg,n,d)
print("RSA signatures same:", sig_rsa1, sig_rsa2)
