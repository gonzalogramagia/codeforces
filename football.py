from collections import Counter

n = int(input())
goals = []
for _ in range(n):
	goals.append(input())

c = Counter(goals)
champion_team = c.most_common(1)[0][0]
print(champion_team)