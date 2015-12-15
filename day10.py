text = "1113222113"

for i in range(50):
	newstring = ""
	place = 0
	while place < len(text):
		number = text[place]
		count = 1
		place += 1
		while place < len(text) and text[place] == number:
			count += 1
			place += 1
		newstring += str(count) + str(number)
	text = newstring
	#print newstring

print len(text)