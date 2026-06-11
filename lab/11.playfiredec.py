import math

letters = 25
total_keys = math.factorial(letters)
power_of_two_total = math.log2(total_keys)

unique_keys = 10**25
power_of_two_unique = math.log2(unique_keys)

print(f"{total_keys:.3e} ≈ 2^{power_of_two_total:.2f}")
print(f"{unique_keys:.3e} ≈ 2^{power_of_two_unique:.2f}")
