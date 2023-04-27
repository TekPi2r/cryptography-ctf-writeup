import hashlib
from Crypto.Cipher import AES

# Known values
plaintext = "I wa"
key = hashlib.sha256("omgwtfbbq".encode()).digest()

# Read ciphertext from file
with open('potential16_ciphers.txt') as f:
    ciphertexts = f.read().splitlines()

# Get IV Function
def get_iv(key, plaintext, ciphertext):
    # Decrypt first block of ciphertext
    cipher = AES.new(key, AES.MODE_CBC, ciphertext)
    decrypted_block = cipher.decrypt(ciphertext)
    
    # XOR decrypted block with plaintext to obtain IV
    iv = bytes([decrypted_block[i] ^ plaintext[i] for i in range(16)])
    return iv.hex()

# Iterate over ciphertexts and try to find the IV
for ciphertext in ciphertexts:
    iv = get_iv(key, plaintext.encode(), ciphertext)
    print(iv)
