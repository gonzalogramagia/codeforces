s = input()

goal = "hello"
i = 0

for l in s:
    if l == goal[i]:
        i += 1
        if i == len(goal):
            break

if i == len(goal):
    print("YES")
else:
    print("NO")