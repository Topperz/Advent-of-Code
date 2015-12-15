f = open("day5input.txt", "r")

total = 0
templist = []
for line in f:
	line = line.rstrip()
	for i in range(len(line)-3):
		check = line[i:i+2]
		if check in line[i+2:]:
			templist.append(line)
			break
for word in templist:
	for i in range(len(word)-2):
		if word[i] == word[i+2]:
			total += 1
			break

print len(templist)
print total