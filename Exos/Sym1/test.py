import base64
import hashlib
from Crypto.Cipher import AES
import itertools

plaintext = "I was lost, but ????????????????"
bs = AES. block_size
key = hashlib. sha256 ("omgwtfbbq".encode()).digest()
iv_string = "????????????????"
# Result shoud be ??374a82db50b23?????b8811d976ddc1cf6db4524aac04e222853969367e0d
resPart1 = "374a82db50b23"
resPart2 = "b8811d976ddc1cf6db4524aac04e222853969367e0d"

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for combination in itertools.product(chars, repeat=16):
    testIv = ''.join(combination)
    iv = testIv.encode()
    cipher = AES.new(key, AES. MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
    hex_ciphertext = ''. join (format (x, '02x') for x in ciphertext)
    print(testIv, ":", hex_ciphertext)
    if resPart1 in hex_ciphertext or resPart2 in hex_ciphertext: print("OK", testIv)