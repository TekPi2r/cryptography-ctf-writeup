tableauChiffre = bytes([0x25, 0x76, 0x30, 0x7B,
                        0x11, 0x91, 0x51, 0x61,
                        0x07, 0x17, 0x70, 0x1E,
                        0x3C, 0x00, 0x00
                      ])

tableauDechiffre = bytes([0x52, 0x49, 0x46, 0x46,   # RIFF
                          0x5C, 0xE2, 0x00, 0x00,   # 57956 - 8
                          0x57, 0x45, 0x42, 0x50,   # WEBP
                          0x56, 0x50, 0x38,   # Magic Number
                        ]) 
resKeyTableau = []

for i in range(len(tableauChiffre)):
  res = tableauChiffre[i] ^ tableauDechiffre[i]
  resKeyTableau.append(res)

key_bytes = bytes(resKeyTableau).hex()
print(key_bytes)
key_ascii = bytes.fromhex(key_bytes).decode('ascii')
print(key_ascii)