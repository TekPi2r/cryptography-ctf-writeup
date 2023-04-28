import hashlib
from Crypto.Cipher import AES
import itertools
import re



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



# Generate all combinations of 8 characters from a-z and 0-9
# chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
chars = '0123456789abcdef'
combinations = itertools.product(chars, repeat=8)

cipher = '??374a82db50b23??????b8811d976ddc1cf6db4524aac04e222853969367e0d'

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

    try:
        # potential_cipher = "33bbe5c24d95e1e0d0afc0909935ffa46b5ec48878b21596a1558f179fdb9908"
        # print("Try potentialCipher:", potential_cipher)
        # print(len(potential_cipher))
        ivRes = get_iv_string(
            "I was lost, but ",
            hashlib.sha256("omgwtfbbq".encode()).digest(),
            potential_cipher
        )
        # print("potentialIvRes:", ivRes)

        block = get_aescbc_block2(
            "I was lost, but ",
            hashlib.sha256("omgwtfbbq".encode()).digest(),
            potential_cipher
        )
        # if contains_letters(block):
        print("potentialBlock:", block)
        print("potentialIvRes:", ivRes)
    except Exception as e:
        continue