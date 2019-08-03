import random

plain_text = list(input("Enter plain text:\n"))
encrypted_text = []
original_text = []
key = []

for i in range(len(plain_text)):
    key.append(chr(random.randint(97, 122)))

for i in range(len(plain_text)):
    encrypted_text.append(chr(((ord(plain_text[i]) + ord(key[i])) % 26) + 97))
    
for i in range(len(plain_text)):
    original_text.append(chr(((ord(plain_text[i]) - ord(key[i])) % 26) + 97))

print(plain_text)
print(key)
print(encrypted_text)
