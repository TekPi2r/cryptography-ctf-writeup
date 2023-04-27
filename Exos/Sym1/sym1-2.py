import base64
import hashlib
from Crypto.Cipher import AES
import threading

plaintext = "I was lost, but "
bs = AES.block_size
key = hashlib.sha256("omgwtfbbq".encode()).digest()
knownciphertext = "374a82db50b23"
knownciphertext2 = "b8811d976dd"

def test_ivs(start, end, threadId):
    print(threadId, " test ", start, end)
    for i in range(start, end):
        iv = i.to_bytes(16, byteorder='big')
        # print(threadId, " test ", iv)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(plaintext.encode())
        hex_ciphertext = ''.join(format(x,'02x') for x in ciphertext)

        if knownciphertext in hex_ciphertext or knownciphertext2 in hex_ciphertext:
            print(f"IV found: {iv}")
            print(f"Ciphertext: {hex_ciphertext}")
            return

# split the loop into 4 threads
num_threads = 256
total_ivs = 256 ** 16
ivs_per_thread = total_ivs // num_threads

threads = []
for i in range(num_threads):
    start = i * ivs_per_thread
    end = start + ivs_per_thread
    t = threading.Thread(target=test_ivs, args=(start, end, i))
    threads.append(t)
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()
