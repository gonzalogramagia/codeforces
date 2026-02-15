a, b = map( int, input().split() )

h = a
r = a

while(r >= b):
	news = r // b
	h += news
	r = news + (r % b)

print(round(h))

