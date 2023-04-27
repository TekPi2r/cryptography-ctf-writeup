import hashlib
from Crypto.Cipher import AES
import itertools



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
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
combinations = itertools.product(chars, repeat=8)

# cipher = '??374a82db50b23??????b8811d976ddc1cf6db4524aac04e222853969367e0d'
cipher = "aa374a82db50b23aaaxi6b8811d976dd"

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
        ivRes = get_iv_string(
            "I was lost, but ",
            hashlib.sha256("omgwtfbbq".encode()).digest(),
            potential_cipher
        )
        if (len(ivRes) == 16):
            print("potentialIvRes:", ivRes)
    except Exception as e:
        continue