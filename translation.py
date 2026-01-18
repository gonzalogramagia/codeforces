s = list(input())
t = list(input())

same_words = True

if len(s) != len(t):
	same_words = False
else:
	i = len(t) - 1

	for letter in s:
		if letter == t[i]:
			i -= 1
			continue
		else:
			same_words = False
			break

if same_words:
	print("YES")
else:
	print("NO")