import base64
import hashlib
from Crypto.Cipher import AES
import os

plaintext = "I was lost, but ????????????????"
bs = AES.block_size
key = hashlib.sha256("omgwtfbbq".encode()).digest()
knownciphertext = "374a82db50b"
knownciphertext2 = "b8811d976ddc1cf6db4524aac04e222853969367e0d"

while True:
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
    hex_ciphertext = ''.join(format(x,'02x') for x in ciphertext)
    if knownciphertext in hex_ciphertext or knownciphertext2 in hex_ciphertext:
        print(f"IV found: {iv}")
        print(f"Ciphertext: {hex_ciphertext}")
        break
