
f = open("text.txt", "r")
lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]
f.close()
f = open("text.txt", "w")
f.writelines(lines)
f.close()