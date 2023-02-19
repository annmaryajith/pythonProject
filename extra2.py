file = open('demo.txt', 'r')
lines = file.readlines()
word_count = 0
for line in lines:
	words = line.split()
	word_count += len(words)
print("Total word count =", word_count)
file.close()