n = int(input())

is_lucky_division = False

for s in range(0,n+1):
	lucky_numbers = { "4", "7" }
	is_lucky_number = True
	for c in list(str(s)):
		if c not in lucky_numbers:
			is_lucky_number = False
			break
	if is_lucky_number:
		if n % s != 0:
			is_lucky_division = False
		else:
			is_lucky_division = True
			break

if is_lucky_division:
	print("YES")
else:
	print("NO")