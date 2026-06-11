def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("No inverse")
    return x % m

n = 3599
e = 31

# Factor n
p = 59
q = 61
phi = (p - 1) * (q - 1)

d = modinv(e, phi)

print("p =", p)
print("q =", q)
print("phi =", phi)
print("Private key d =", d)
