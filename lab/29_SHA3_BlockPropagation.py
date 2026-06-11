# Simulation of SHA-3 lane filling with 1024-bit block size
# We ignore permutation as instructed.

# SHA-3 state: 5x5 lanes, each lane is 64 bits
lanes = [[0 for _ in range(5)] for _ in range(5)]

# Capacity portion: assume half of the lanes (for 1024-bit capacity) start as zero
capacity_lanes = [(i,j) for i in range(5) for j in range(5)][12:]  # 13 lanes ~ 832 bits, close to 1024
for i,j in capacity_lanes:
    lanes[i][j] = 0

# Message block P0: assume each lane in the rate portion has at least one nonzero bit
for i,j in [(i,j) for i in range(5) for j in range(5) if (i,j) not in capacity_lanes]:
    lanes[i][j] = 1

# Track how many rounds until all capacity lanes get nonzero bits
rounds = 0
while any(lanes[i][j] == 0 for i,j in capacity_lanes):
    rounds += 1
    # Simplified mixing: each round, every zero lane gets influenced by a nonzero lane
    for i,j in capacity_lanes:
        lanes[i][j] = 1

print("Rounds until all capacity lanes nonzero:", rounds)
