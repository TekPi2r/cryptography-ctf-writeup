import sys

def xor_file(infile, outfile, key):
    with open(infile, "rb") as f:
        data = f.read()

    # XOR operation
    xor_data = bytearray()
    for i in range(len(data)):
        xor_data.append(data[i] ^ key[i % len(key)])

    # Write XOR data to output file
    with open(outfile, "wb") as f:
        f.write(xor_data)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python xor_bmp.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    key = bytes('gitgud'.encode())

    xor_file(input_file, output_file, key)
