from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import inverse
from functools import reduce
from math import isqrt

# Read the encrypted message from the text file
with open('./rsa2ez4me/cipher.txt', 'rb') as f:
    ciphertext = f.read()

# Convert the ciphertext bytes to an integer
ciphertext_int = int.from_bytes(ciphertext, byteorder='big')
# print(ciphertext_int)

n_list = []

# Read the public key from the PEM file
for i in range(100):
    # Read the public key from the PEM file
    with open(f'./rsa2ez4me/keys/pub{i}.pem', 'r') as f:
        key = RSA.import_key(f.read())
        n_list.append(key.n)
print("Finish to insert n")

# Fonction pour factoriser un nombre avec l'algorithme de Fermat
def fermat_factor(n):
    a = isqrt(n) + 1
    b2 = a*a - n
    while not is_square(b2):
        a += 1
        b2 = a*a - n
    p = a + isqrt(b2)
    q = a - isqrt(b2)
    return p, q

# Fonction pour vérifier si un nombre est un carré parfait
def is_square(n):
    return isqrt(n)**2 == n

# Trouver le facteur primaire commun
p = 1
for n in n_list:
    p_, q_ = fermat_factor(n)
    if p == 1:
        p = p_
    else:
        assert p == p_
print("Le facteur primaire commun est:", p)
