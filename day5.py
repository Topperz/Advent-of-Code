import re

f = open("day5input.txt", "r")

check1 = re.compile(r'(.)\1')
check2 = re.compile(r"ab|cd|pq|xy")
vowels = ["a","e","i","o","u"]

total = 0

for line in f:
	line = line.rstrip()
	count = 0
	for i in line:
		if i in vowels:
			count += 1
	if count >= 3:
		result = re.findall(check1, line)
		if result:
			result2 = re.findall(check2, line)
			if not result2:
				total += 1

print total



