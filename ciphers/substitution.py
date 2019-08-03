plain_text = list(input("Enter plain text:\n"))
encrypted_text = []
original_text = []

for char in plain_text:
    encrypted_text.append(chr(ord(char)+5))

for char in encrypted_text:
    original_text.append(chr(ord(char)-5))

print(encrypted_text)
print(original_text)