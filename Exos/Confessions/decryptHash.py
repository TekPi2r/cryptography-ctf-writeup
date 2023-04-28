import string
import hashlib

hashes_file = 'hashes.txt'

with open(hashes_file, 'r') as f:
    hashes = [line.strip() for line in f]

charset = string.ascii_letters + string.digits + string.punctuation
flag = ""  # Replace with whatever prefix or suffix you want to use

for i in hashes:
    for x in charset:
        if hashlib.sha256(flag.encode() + x.encode()).hexdigest() == i:
            flag += x
            break

print(flag)  # Prints the flag that was found
