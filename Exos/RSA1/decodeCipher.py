from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Read the public key from the PEM file
with open('rsa1.pem', 'r') as f:
    key = RSA.import_key(f.read())

# Factorize the modulus N using the given number p
p = 11901234461494228310064076121482038286429650089208969229876184007349956782094248940290427800597817633601014470221576037327691902428151823981665392121868907
q = key.n // p

# Compute the private exponent d
phi = (p - 1) * (q - 1)
d = pow(key.e, -1, phi)

# Read the encrypted message from the text file
with open('rsa1Cipher.txt', 'rb') as f:
    ciphertext = f.read()

# Decrypt the message using the private key
private_key = RSA.construct((key.n, key.e, d, p, q))
cipher = PKCS1_OAEP.new(private_key)
plaintext = cipher.decrypt(ciphertext)

# Print the decrypted message
print(plaintext.decode())
