word = input()

result = ""

for letter in word:
	if letter.lower() in "aeiyou":
		continue
	else:
		result+="."
		result+=letter.lower()

print(result)