import heapq

f = open("day2input.txt", "r")

def surface(l,w,h):
	a = 2*l*w
	b = 2*w*h
	c = 2*h*l
	return a+b+c + min(a/2,b/2,c/2)

def ribbon(l,w,h):
	dim = [l,w,h]
	twolowest = heapq.nsmallest(2,dim)
	around = twolowest[0]*2 + twolowest[1]* 2
	rib = l*w*h
	return around + rib

total = 0
ribbonlength = 0

for line in f:
	line = line.rstrip().split("x")
	l = int(line[0])
	w = int(line[1])
	h = int(line[2])

	total += surface(l,w,h)
	ribbonlength += ribbon(l,w,h)

print total
print ribbonlength


f.close()