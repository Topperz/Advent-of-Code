
f = open("day7input.txt", "r")

calculated = {}
results = {}

for line in f:
	line = line.rstrip()
	instruction, result = line.split("->")
	calculated[result.strip()] = instruction.strip().split(" ")
	
f.close
def calculate(name):
	try:
		return int(name)
	except ValueError:
		pass

	if name not in results:
		instructions = calculated[name]
		if len(instructions) == 1:
			result = calculate(instructions[0])
		else:
			operator = instructions[-2]
			if operator == "AND":
				result = calculate(instructions[0]) & calculate(instructions[2])
			elif operator == "OR":
				result = calculate(instructions[0]) | calculate(instructions[2])
			elif operator == "NOT":
				result = ~calculate(instructions[1])
			elif operator == "RSHIFT":
				result = calculate(instructions[0]) >> calculate(instructions[2])
			elif operator == "LSHIFT":
				result = calculate(instructions[0]) << calculate(instructions[2])
		results[name] = result
	return results[name]

firstresult = calculate("a")
print firstresult
calculated["b"] = [str(firstresult)]
results.clear()
secondresult = calculate("a")
print secondresult