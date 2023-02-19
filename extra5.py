
with open('demo.txt','r') as f1, open('alphabets.txt','r') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

for line1, line2 in zip(lines1, lines2):
    print(line1.strip() + ' ' + line2.strip())