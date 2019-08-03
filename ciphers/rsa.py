import random
from halo import Halo

def is_prime(num):
    ans = True
    for i in range(2, num):
        if num % i == 0:
            ans = False
            break
    return ans


def key_gen():
    spinner = Halo(text="Generating key...", spinner="dots")
    spinner.start()
    
    primes = [i for i in range(1000, 10000) if is_prime(i)]
    p = random.choice(primes)
    q = random.choice(primes)
    n = p * q
    fn = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, n)
        if e % 2 == 1:
            relatively_prime = True
            for i in range(2, e):
                if e % i == 0 and fn % i == 0:
                    relatively_prime = False
                    break
            if relatively_prime:
                break

    d = (e ** -1) % fn
    public_keys = [e, n]
    private_keys = [d, n]

    spinner.stop()
    print("Key generated")
    
    return [public_keys, private_keys]


def encrypt(text):
    keys = key_gen()
    public_keys = keys[0]
    private_keys = keys[1]
    
    spinner = Halo(text="Encrypting...", spinner="dots")
    spinner.start()
    
    e = public_keys[0]
    n = public_keys[1]
    cipher_text = (text ** e) % n

    spinner.stop()
    print("Encryption completed")
    
    return [cipher_text, private_keys]


def decrypt(rsa):
    spinner = Halo(text="Decrypting...", spinner="dots")
    spinner.start()
    
    cipher_text = rsa[0]
    private_keys = rsa[1]

    d = private_keys[0]
    n = private_keys[1]

    original_text = (cipher_text ** d) % n
    # original_text = [chr(char) for char in ascii_text]

    spinner.stop()
    print("Decryption completed")
    
    return original_text


plain_text = int(input("Enter plain text:\n"))
# ascii_text = [ord(char) for char in plain_text]
rsa = encrypt(plain_text)

cipher_text = rsa[0]
print(f"Cipher text is {cipher_text}")

original_text = decrypt(rsa)
print(f"Original text is {original_text}")