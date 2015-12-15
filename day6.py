f = open("day6input.txt", "r")

gridsize = 1000
grid = []

for row in range(gridsize):
	grid.append([])
	for column in range(gridsize):
		grid[row].append(0)

for line in f:
	line = line.rstrip()
	line = line.split(" ")

	if "on" in line:
		firstcoord = line[2].split(",")
		secondcoord = line[4].split(",")
		for row in range(int(firstcoord[0]), int(secondcoord[0])+1):
			for column in range(int(firstcoord[1]), int(secondcoord[1])+1):
				grid[column][row] = 1

	if "off" in line:
		firstcoord = line[2].split(",")
		secondcoord = line[4].split(",")
		for row in range(int(firstcoord[0]), int(secondcoord[0])+1):
			for column in range(int(firstcoord[1]), int(secondcoord[1])+1):
				grid[column][row] = 0

	if "toggle" in line:
		firstcoord = line[1].split(",")
		secondcoord = line[3].split(",")
		for row in range(int(firstcoord[0]), int(secondcoord[0])+1):
			for column in range(int(firstcoord[1]), int(secondcoord[1])+1):
				if grid[column][row] == 1:
					grid[column][row] = 0
				elif grid[column][row] == 0:
					grid[column][row] = 1

total = 0

for row in range(gridsize):
	for column in range(gridsize):
		total += grid[column][row]

print total

f.close

