def generate_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    seen = set()
    matrix = []
    for char in keyword:
        if char.isalpha() and char not in seen:
            matrix.append(char)
            seen.add(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def playfair_decrypt(ciphertext, matrix):
    ciphertext = ciphertext.upper().replace("J", "I").replace(" ", "")
    if len(ciphertext) % 2 != 0:
        raise ValueError("Ciphertext length must be even.")
    result = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row
            result += matrix[row1][(col1 - 1) % 5]
            result += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            result += matrix[(row1 - 1) % 5][col1]
            result += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle swap
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    return result

keyword = "PLAYFAIR"
matrix = generate_matrix(keyword)

ciphertext = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
plaintext = playfair_decrypt(ciphertext, matrix)

print("Playfair Matrix:")
for row in matrix:
    print(row)
print("\nDecrypted Plaintext:\n", plaintext)
