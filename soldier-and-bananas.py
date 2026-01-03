cost, dollars, bananas = map( int, input().split() )

total = 0
borrow = 0

for i in range(1, bananas + 1):
	total += cost * i

if(total > dollars):
	borrow = total - dollars

print(borrow)


