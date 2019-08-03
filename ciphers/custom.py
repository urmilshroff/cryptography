class CustomCipher:
    def __init__(self):
        self.encrypted_text = []
        self.decrypted_text = []

    def encrypt(self, plain_text):
        for char in plain_text:
            encrypted_char = chr(ord(char) + len(plain_text))
            self.encrypted_text.append(encrypted_char)

    def decrypt(self, cipher_text):
        for char in cipher_text:
            decrypted_char = chr(ord(char) - len(cipher_text))
            self.decrypted_text.append(decrypted_char)


cipher = CustomCipher()
choice = int(
    input("What would you like to do?\n1. Encrypt text\n2. Decrypt text\n"))

if choice == 1:
    cipher.encrypt(list(input("Enter text to encrypt:\n")))
    print(f"Encrypted text is {cipher.encrypted_text}")

elif choice == 2:
    cipher.decrypt(list(input("Enter text to decrypt:\n")))
    print(f"Decrypted text is {cipher.decrypted_text}")

else:
    print("Error: bad input!")
