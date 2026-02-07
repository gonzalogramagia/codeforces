n = int(input())

min_inception_bacterias = 0

while n > 0:
	if n % 2 == 1:
		min_inception_bacterias += 1
	n //= 2

print(min_inception_bacterias)