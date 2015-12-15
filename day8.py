import re

f = open("day8input.txt", "r")
number_of_dubbledash = 0
number_of_quotes = 0
number_of_hexes = 0
number_of_chars = 0
total = 0
totaleval = 0
for line in f:
	line = line.rstrip()

	dubbledash = re.findall(r"\\\\", line)
	quote = re.findall(r'\\"', line[:-1])
	hexes = re.findall(r"\\x[0-9a-f][0-9a-f]", line)
	number_of_dubbledash += len(dubbledash)
	number_of_quotes += len(quote)
	number_of_hexes += len(hexes)
	number_of_chars += len(line)
	print dubbledash
	print quote
	print hexes
	print len(line)
	print len(line) - 2 - len(dubbledash) - len(quote) - len(hexes)*3
	total += len(line) - 2 - len(dubbledash) - len(quote) - len(hexes)*3

	totaleval += len(line) - len(eval(line))
	print len(eval(line))


print number_of_chars - total
print totaleval
