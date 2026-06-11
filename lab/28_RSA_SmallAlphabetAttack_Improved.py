def modexp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

# Public parameters
q = 23
a = 5

# Alice and Bob choose secret numbers
xA = 6
xB = 15

# Normal Diffie-Hellman exchange
A = modexp(a, xA, q)
B = modexp(a, xB, q)

# Shared key
KA = modexp(B, xA, q)
KB = modexp(A, xB, q)

print("Alice sends:", A)
print("Bob sends:", B)
print("Shared key Alice:", KA)
print("Shared key Bob:", KB)

# If they mistakenly send x*a instead of a^x mod q
A_wrong = (xA * a) % q
B_wrong = (xB * a) % q
print("Alice sends wrong:", A_wrong)
print("Bob sends wrong:", B_wrong)
