def generate_matrix_from_list(matrix_list):
    return [matrix_list[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    if char == 'J':  
        char = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def preprocess_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            digraphs.append(a + 'X')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    return digraphs

def playfair_encrypt(plaintext, matrix):
    digraphs = preprocess_text(plaintext)
    result = ""
    for pair in digraphs:
        a, b = pair[0], pair[1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  
            result += matrix[row1][(col1 + 1) % 5]
            result += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # same column
            result += matrix[(row1 + 1) % 5][col1]
            result += matrix[(row2 + 1) % 5][col2]
        else:  # rectangle
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    return result

matrix_list = ['M','F','H','I','K',
               'U','N','O','P','Q',
               'Z','V','W','X','Y',
               'E','L','A','R','G',
               'D','S','T','B','C']

matrix = generate_matrix_from_list(matrix_list)

plaintext = "Must see you over Cadogan West. Coming at once."
ciphertext = playfair_encrypt(plaintext, matrix)

print("Playfair Matrix:")
for row in matrix:
    print(row)
print("\nCiphertext:\n", ciphertext)
