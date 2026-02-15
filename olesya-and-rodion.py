n, t = map( int, input().split() )

start = 10**(n-1)
end = (10**n)

result = -1

for number in range(start, end):
	if number % t == 0:
		result = number
		break

print(result)
