digits = list(input())

lucky_numbers = sum(1 for d in digits if d in ('4','7'))

if lucky_numbers == 4 or lucky_numbers == 7:
	print("YES")
else:
	print("NO")