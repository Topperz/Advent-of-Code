import hashlib

puzzle_input = "yzbqklnj"

number = 0

# while True:
# 	string = puzzle_input + str(number)
# 	out = hashlib.md5(string).hexdigest()
# 	if out.startswith("00000"):
# 		print number
# 		break
# 	else:
# 		number += 1

###### Part 2

while True:
	string = puzzle_input + str(number)
	out = hashlib.md5(string).hexdigest()
	if out.startswith("000000"):
		print number
		break
	else:
		number += 1