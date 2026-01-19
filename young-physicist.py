n = int( input() )

totals = {}
total_x = 0
total_y = 0
total_z = 0

for i in range(n):
	totals[i] = list ( map( int, input().split() ) )

for _, values in totals.items():
	total_x += values[0]
	total_y += values[1]
	total_z += values[2]

if total_x == 0 and total_y == 0 and total_z == 0:
	print("YES")
else:
	print("NO")