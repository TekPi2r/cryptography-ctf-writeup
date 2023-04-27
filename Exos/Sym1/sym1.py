import base64
import hashlib
from Crypto.Cipher import AES
import os

plaintext = "I was lost, but "
bs = AES.block_size
key = hashlib.sha256("omgwtfbbq".encode()).digest()
knownciphertext = "374a82db50b23"
knownciphertext2 = "b8811d976dd"

while True:
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
    hex_ciphertext = ''.join(format(x,'02x') for x in ciphertext)
    hex_iv = ''.join(format(x,'02x') for x in iv)
    print(hex_iv)
    if knownciphertext in hex_ciphertext or knownciphertext2 in hex_ciphertext:
        print(f"IV found: {iv}")
        print(f"Ciphertext: {hex_ciphertext}")
        break
