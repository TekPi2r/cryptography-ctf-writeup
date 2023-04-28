tableauChiffre = bytes([0x25, 0x24, 0xEE, 0x9F, 0x75, 0x64]) # Premier bytes du fichier ch2.bmp en little endian
tableauDechiffre = bytes([0x42, 0x4D, 0x9A, 0xF8, 0x00, 0x00]) # Premier bytes d'un fichier BMP en little endian
resKeyTableau = []

for i in range(len(tableauChiffre)):
    res = tableauChiffre[i] ^ tableauDechiffre[i]
    resKeyTableau.append(res)

key_bytes = bytes(resKeyTableau).hex()
print(key_bytes)
key_ascii = bytes.fromhex(key_bytes).decode('ascii')
print(key_ascii)