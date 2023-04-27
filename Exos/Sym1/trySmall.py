import threading
import hashlib
from Crypto.Cipher import AES
import re
import random



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

new_cipher = list('??374a82db50b23??????b8811d976ddc1cf6db4524aac04e222853969367e0d')

def generate_hex_values(start, end, threadId):
    print("ThreadId:", threadId)
    while True:
        i = random.randint(start, end)
        hex_val = hex(i)[2:].zfill(8)
        new_cipher[0] = hex_val[0]
        new_cipher[1] = hex_val[1]
        new_cipher[15] = hex_val[2]
        new_cipher[16] = hex_val[3]
        new_cipher[17] = hex_val[4]
        new_cipher[18] = hex_val[5]
        new_cipher[19] = hex_val[6]
        new_cipher[20] = hex_val[7]
        potential_cipher = ''.join(new_cipher)
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
            if contains_letters(block):
                print("potentialBlock:", block)
                print("potentialIvRes:", ivRes)
                break
        except Exception as e:
            pass

# Split the work among 4 threads
num_threads = 1024
total_values = 256**4
values_per_thread = total_values // num_threads

# Create and start the threads
threads = []
for i in range(num_threads):
    start = i * values_per_thread
    end = (i + 1) * values_per_thread
    t = threading.Thread(target=generate_hex_values, args=(start, end, i))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()