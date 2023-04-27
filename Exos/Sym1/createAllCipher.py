import itertools

# Generate all combinations of 8 characters from a-z and 0-9
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
combinations = itertools.product(chars, repeat=3)

cipher = '??374a82db50b23?'

# Print all combinations
with open('potential16_ciphers.txt', 'w') as f:
    for combo in combinations:
        new_cipher = list(cipher)  # Convert string to a list of characters to modify it
        new_cipher[0] = combo[0]
        new_cipher[1] = combo[1]
        new_cipher[15] = combo[2]
        potential_cipher = ''.join(new_cipher)  # Convert list of characters back to a string
        # print(potential_cipher)
        f.write(potential_cipher + '\n')  # Write cipher to file
