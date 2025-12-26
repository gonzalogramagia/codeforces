from collections import Counter

username = input()

c = Counter(username)

if len(c) % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")	