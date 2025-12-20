n = int(input())	# 1 <= n <= 150

result = 0

for _ in range(n):
	character = input()
	match character[0]:
		case "X":
			if character[1] == "+":
				result += 1
			else:
				result -= 1
		case "+":
			result += 1
		case "-":
			result -= 1

print(result)
