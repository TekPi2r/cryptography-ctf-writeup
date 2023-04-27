import hashlib
from Crypto.Cipher import AES

# Known values
plaintext = "I was lost, but "
key = hashlib.sha256("omgwtfbbq".encode()).digest()
ciphertext = "aa374a82db50b23aaaaafb8811d976dd".encode()

# Decrypt first block of ciphertext
cipher = AES.new(key, AES.MODE_CBC, ciphertext[:AES.block_size])
decrypted_block = cipher.decrypt(ciphertext[:AES.block_size])

# XOR decrypted block with plaintext to obtain IV
iv = bytes([decrypted_block[i] ^ ord(plaintext[i]) for i in range(AES.block_size)])

print(iv.hex())
