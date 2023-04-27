import hashlib
from Crypto.Cipher import AES

def encode_aescbc(plaintext, key, iv):
    bs = AES.block_size
    # Pad the plaintext to a multiple of block size using PKCS#7 padding
    padded_plaintext = plaintext.encode() + (bs - len(plaintext) % bs) * chr(bs - len(plaintext) % bs).encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_plaintext)
    # Encode the ciphertext in hexadecimal
    hex_ciphertext = ciphertext.hex()
    return hex_ciphertext


def get_iv_string(plaintext, key, ciphertext):
    bs = AES.block_size
    # Decode the hexadecimal-encoded ciphertext
    ciphertext = bytes.fromhex(ciphertext)
    # Extract the IV from the first block of the ciphertext
    iv = ciphertext[:bs]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the first block of the ciphertext to get the original IV
    decrypted_block = cipher.decrypt(ciphertext[:bs])
    iv_string = ''.join([chr(decrypted_block[i] ^ iv[i] ^ plaintext.encode()[i]) for i in range(bs)])
    return iv_string


finalIv = "helloworlditsmee".encode()
ciphertextRes = encode_aescbc(
    "I was lost, but i find the solve",
    hashlib.sha256("omgwtfbbq".encode()).digest(),
    finalIv
)
print(ciphertextRes)

ivRes = get_iv_string(
    "I was lost, but i find the solve",
    hashlib.sha256("omgwtfbbq".encode()).digest(),
    ciphertextRes
)
print(ivRes)
# ivRes value expected is "helloworlditsmee"
