
with open('alphabets.txt', 'r') as source_file:
    with open('target_file.txt', 'w') as target_file:
        for line in source_file:
            target_file.write(line)
print('File copied successfully!')