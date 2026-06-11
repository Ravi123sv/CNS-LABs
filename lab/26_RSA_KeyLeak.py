import sympy

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

# Example modulus
n = 3599
e = 31
factors = sympy.factorint(n)
p, q = list(factors.keys())
phi = (p-1)*(q-1)

# Suppose Bob leaks d
d = modinv(e, phi)
print("Leaked private key d =", d)

# Attacker can factor n
print("Factors of n:", p, q)

# Attacker can generate new (e,d) pairs
new_e = 17
new_d = modinv(new_e, phi)
print("Attacker recomputes new keys:", new_e, new_d)

print("Conclusion: Changing e,d with same n is unsafe. New modulus required.")
