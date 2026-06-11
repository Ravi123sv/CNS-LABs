def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()
    for c in key:
        if c.isalpha() and c not in used:
            matrix.append(c)
            used.add(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J merged with I
        if c not in used:
            matrix.append(c)
            used.add(c)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

key = input("Enter keyword: ")
matrix = generate_matrix(key)
print("Playfair Matrix:")
print_matrix(matrix)
