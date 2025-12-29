n = int( input() )

colors = input()

removes = 0

for i in range(n-1):
	if colors[i] == colors[i+1]:
		removes += 1

print(removes)
