nk = input().split()
n = int(nk[0])
k = int(nk[1])

# better alternative: n, k = map(int, input().split())

scores = list(map(int, input().split()))
kth_score = scores[k-1]

i = 0

for score in scores:
	if score < kth_score or score == 0:
		break
	i += 1

print(i)