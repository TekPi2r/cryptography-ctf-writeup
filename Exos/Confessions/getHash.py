import json

input_file = 'requestLog.json'  # Replace with the name of your JSON file
output_file = 'hashes.txt'  # Replace with the name of the output file you want to create

with open(input_file, 'r') as f:
    data = json.load(f)

hashes = []  # A list to store all the hash values

with open(output_file, 'w') as f:
    for log in data['data']['requestsLog']:
        args = json.loads(log['args'])  # Parse the "args" field as JSON
        if 'hash' in args:
            hashes.append(args['hash'])  # Append the "hash" value to the list
            f.write(args['hash'] + '\n')  # Write each hash value to a new line in the output file
            # f.write('\"' + args['hash'] + '\"' + '\n')  # Write each hash value to a new line in the output file
