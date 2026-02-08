n = int(input())

for _ in range(n):
	_ = int(input())
	s = input()
	balance = 0
	moves = 0

	for c in s:
		if c == '(':
			balance += 1
		else:  # ')'
			if balance > 0:
				balance -= 1
			else:
				moves += 1
    
	print(moves)