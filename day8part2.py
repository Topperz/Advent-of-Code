import re

f = open("day8input.txt", "r")

number_of_chars = 0
total = 0
totaleval = 0
reescapetotal = 0
for line in f:
	line = line.rstrip()
	dubbledash = re.findall(r"\\\\", line)
	quote = re.findall(r'\\"', line[:-1])
	hexes = re.findall(r"\\x[0-9a-f][0-9a-f]", line)

	number_of_chars += len(line)
	total += len(line) + 4 + len(dubbledash)*2 + len(quote)*2 + len(hexes)

	totaleval += len(line) - len(eval(line))
	reescapetotal += len(re.escape(line)) + 2

print total - number_of_chars 
print totaleval
print reescapetotal - number_of_chars
# stringdata = len string