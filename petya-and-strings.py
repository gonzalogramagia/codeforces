first_string = input()
second_string = input()

n = len(first_string)

comparision = 0

for i in range(n):
	if first_string[i].lower() != second_string[i].lower():
		if first_string[i].lower() < second_string[i].lower():
			comparision = -1
		else:
			comparision = 1
		break

print(comparision)