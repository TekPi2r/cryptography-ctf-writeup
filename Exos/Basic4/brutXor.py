tableauChiffre = bytes([0x25, 0x76, 0x30, 0x7B,
                        0x11, 0x91, 0x51, 0x61,
                        0x07, 0x17, 0x70, 0x1E])

tableauDechiffre = bytes([0x52, 0x49, 0x46, 0x46,   # RIFF
                          0xE2, 0x04, 0x00, 0x00,   # 57956
                          0x57, 0x45, 0x42, 0x50])  # WEBP
resKeyTableau = []

for i in range(len(tableauChiffre)):
  res = tableauChiffre[i] ^ tableauDechiffre[i]
  resKeyTableau.append(res)

key_bytes = bytes(resKeyTableau).hex()
print(key_bytes)