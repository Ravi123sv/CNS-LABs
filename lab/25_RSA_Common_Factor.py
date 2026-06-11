import math

n = 77   # example modulus
block = 7  # example plaintext block

g = math.gcd(n, block)

print("n =", n)
print("block =", block)
print("gcd =", g)

if g > 1:
    print("This gcd reveals a factor of n:", g)
    print("RSA can be broken by factoring n using this.")
else:
    print("No useful factor found.")
