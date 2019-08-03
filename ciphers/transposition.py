import math
import numpy as np

plain_text = list(input("Enter plain text:\n"))
key = int(input("Enter key:\n"))

cols = key
rows = math.ceil(len(plain_text) / key)

crypto_grid = np.chararray((rows, cols), unicode=True)

pos = 0
for row in range(rows):
    for col in range(cols):
        if pos < len(plain_text):
            crypto_grid[row, col] = plain_text[pos]
            pos += 1
        else:
            break

original_text = []
encrypted_text = []
rows = crypto_grid.shape[0]
cols = crypto_grid.shape[1]

for col in range(cols):
    for row in range(rows):
        encrypted_text.append(crypto_grid[row, col])

for row in range(rows):
    for col in range(cols):
        original_text.append(crypto_grid[row, col])

print(f"Plain text: {plain_text}")
print(f"Crypto grid: {crypto_grid}")
print(f"Encrypted text: {encrypted_text}")
print(f"Original text: {original_text}")
