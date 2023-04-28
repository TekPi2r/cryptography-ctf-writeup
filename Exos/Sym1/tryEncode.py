import hashlib
from Crypto.Cipher import AES



def xor(plaintext, payload):
    len_PT = len(plaintext)
    res = []

    for i in range(0, len(payload)):
        res.append(payload[i] ^ plaintext[i % len_PT])
    return bytes(res)



def encode_aescbc(plaintext, key, iv):
    bs = AES.block_size
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
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



def new_get_iv_string(plaintext, key, ciphertext):
    bs = AES.block_size
    ciphertextBytes = bytes.fromhex(ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    payload = cipher.decrypt(ciphertextBytes)
    iv = xor(plaintext, payload).decode()
    return iv



def get_aescbc_block2(plaintext, key, ciphertext):
    bs = AES.block_size
    # Decode the hexadecimal-encoded ciphertext to bytes
    ciphertext = bytes.fromhex(ciphertext)
    # Extract the IV from the first block of the ciphertext
    iv = ciphertext[:bs]
    # Create a new AES cipher instance with the given key and extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the ciphertext using the new cipher instance
    decrypted_plaintext = cipher.decrypt(ciphertext)
    # Extract the desired block from the decrypted plaintext and return it
    block = decrypted_plaintext[bs:2*bs]
    return block.decode()





finalIv = "aaaaaaaaaaaaaaaa".encode()
ciphertextRes = encode_aescbc(
    "I was lost, but i find the solve",
    hashlib.sha256("omgwtfbbq".encode()).digest(),
    finalIv
)
print(ciphertextRes)
print("len of ciphertext", len(ciphertextRes))
print()
# 33bbe5c24d95e1e0d0afc0909935ffa46b5ec48878b21596
# a1558f179fdb990832b9bab43c0d1308747d4330581c7afd



# ivRes = get_iv_string(
#     "I was lost, but ",
#     hashlib.sha256("omgwtfbbq".encode()).digest(),
#     ciphertextRes
# )
# print(ivRes)
# print("len of ivRes", len(ivRes))
# print()
ivRes = new_get_iv_string(
    b"I was lost, but ",
    hashlib.sha256("omgwtfbbq".encode()).digest(),
    ciphertextRes[:32]
)
print(ivRes)
print()
# ivRes value expected is "aaaaaaaaaaaaaaaa"



block = get_aescbc_block2(
    "I was lost, but ",
    hashlib.sha256("omgwtfbbq".encode()).digest(),
    "33bbe5c24d95e1e0d0afc0909935ffa46b5ec48878b21596a1558f179fdb9908"
)
print(block)
print()
# Expected value "i find the solve"