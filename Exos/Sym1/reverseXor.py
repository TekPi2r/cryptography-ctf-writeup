import hashlib
from Crypto.Cipher import AES

import itertools

def tryIv(hexaCipher):
    # Known values
    plaintext = "I was lost, but "
    key = hashlib.sha256("omgwtfbbq".encode()).digest()
    ciphertext = hexaCipher.encode()

    bs = AES.block_size

    # Decrypt first block of ciphertext
    cipher = AES.new(key, AES.MODE_CBC, ciphertext[:bs])
    decrypted_block = cipher.decrypt(ciphertext[:bs])

    # XOR decrypted block with plaintext to obtain IV
    iv = bytes([decrypted_block[i] ^ plaintext.encode()[i] for i in range(bs)])

    # print(iv.hex())

    cipherReal = AES.new(key, AES. MODE_CBC, iv)
    ciphertextReal = cipherReal.encrypt(plaintext.encode())
    hex_ciphertextReal = ''. join (format (x, '02x') for x in ciphertextReal)

    if (hex_ciphertextReal == hexaCipher):
        print("SUCCESS")
        print(iv)
    # print(hex_ciphertextReal)
    # Should be equal to ciphertext in line 8


# Generate all combinations of 8 characters from a-z and 0-9
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
combinations = itertools.product(chars, repeat=8)

cipher = '??374a82db50b23??????b8811d976dd'

# Print all combinations
for combo in combinations:
    new_cipher = list(cipher)  # Convert string to a list of characters to modify it
    new_cipher[0] = combo[0]
    new_cipher[1] = combo[1]
    new_cipher[15] = combo[2]
    new_cipher[16] = combo[3]
    new_cipher[17] = combo[4]
    new_cipher[18] = combo[5]
    new_cipher[19] = combo[6]
    new_cipher[20] = combo[7]
    potential_cipher = ''.join(new_cipher)  # Convert list of characters back to a string
    tryIv(potential_cipher)