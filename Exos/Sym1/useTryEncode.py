import hashlib
from Crypto.Cipher import AES
import itertools
import re



def xor(plaintext, payload):
    len_PT = len(plaintext)
    res = []

    for i in range(0, len(payload)):
        res.append(payload[i] ^ plaintext[i % len_PT])
    return bytes(res)



def contains_letters(s):
    # Define a regular expression pattern that matches any character from a to z, case-insensitive
    pattern = re.compile(r'[a-zA-Z]')
    # Search for the pattern in the input string
    match = pattern.search(s)
    # If a match is found, return True, otherwise return False
    if match:
        return True
    else:
        return False



def encode_aescbc(plaintext, key, iv):
    bs = AES.block_size
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
    # Encode the ciphertext in hexadecimal
    hex_ciphertext = ciphertext.hex()
    return hex_ciphertext



def new_get_iv_string(plaintext, key, ciphertext):
    bs = AES.block_size
    ciphertextBytes = bytes.fromhex(ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    payload = cipher.decrypt(ciphertextBytes)
    iv = xor(plaintext, payload).decode()
    return iv



def get_aescbc_block2(key, ciphertext):
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



# Generate all combinations of 8 characters from a-z and 0-9
# chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
chars = '0123456789abcdef'
combinations = itertools.product(chars, repeat=7)

cipher = '??f374a82db50b23?????b88f1d976dd'

# Print all combinations
for combo in combinations:
    potential_cipher = f"{combo[0] + combo[1]}f374a82db50b23{combo[2] + combo[3] + combo[4] + combo[5] + combo[6]}b88f1d976dd"
    try:
        # potential_cipher = "33bbe5c24d95e1e0d0afc0909935ffa46b5ec48878b21596a1558f179fdb9908"
        # print("Try potentialCipher:", potential_cipher)
        # print(len(potential_cipher))
        ivRes = new_get_iv_string(
            b"I was lost, but ",
            hashlib.sha256("omgwtfbbq".encode()).digest(),
            potential_cipher
        )
        if ivRes.isprintable() and len(ivRes) == 16:
            print("potentialIvRes:", ivRes)
            # h4ppyh4ppya5canB
            print("potentialCipher", potential_cipher)
            # 02f374a82db50b23a7d09b88f1d976dd
            block = get_aescbc_block2(
                hashlib.sha256("omgwtfbbq".encode()).digest(),
                potential_cipher + "c1cf6db4524aac04e222853969367e0d"
            )
            print(block)
            print()

    except Exception as e:
        continue