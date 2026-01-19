n = int(input())

for year in range(n+1, 10000):
	current_year = list(str(year))
	if len( set(current_year) ) == 4:
		print(year)
		break