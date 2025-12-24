matrix = []

one_position = tuple()

swaps = 0

for row in range(5):
	matrix.append( list( map( int, input().split() ) ) )
	for column in range(5):
		if matrix[row][column] == 1:
			one_position = (column, row)

swaps = abs(one_position[0] - 2) + abs(one_position[1] - 2)

print(swaps)