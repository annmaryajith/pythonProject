with open('alphabets.txt', 'w') as f:
    for i in range(1, 27, 2):
        alphabet = chr(i+64) + chr(i+65)
        f.write(alphabet + "\n")