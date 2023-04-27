import base64
import hashlib
from Crypto.Cipher import AES

plaintext = "I was lost, but ????????????????"
bs = AES. block_size
key = hashlib.sha256 ("omgwtfbbq".encode()).digest()
iv_string = "????????????????"
# Result shoud be ??374a82db50b23?????b8811d976ddc1cf6db4524aac04e222853969367e0d
resPart1 = "374a82db50b23"
resPart2 = "b8811d976ddc1cf6db4524aac04e222853969367e0d"
iv = iv_string.encode()
cipher = AES.new(key, AES. MODE_CBC, iv)
ciphertext = cipher.encrypt(plaintext.encode())
hex_ciphertext = ''. join (format (x, '02x') for x in ciphertext)
print(hex_ciphertext)
if resPart1 in hex_ciphertext or resPart2 in hex_ciphertext: print("OK")