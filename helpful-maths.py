numbers = list( map( int, input().split("+") ) )

swaps = -1

while(swaps != 0):
	swaps = 0
	for i in range(len(numbers)-1):
		if numbers[i] > numbers[i+1]:
			aux = numbers[i]
			numbers[i] = numbers[i+1]
			numbers[i+1] = aux
			swaps += 1

result = "+".join(list(map(str,numbers)))

print(result)

