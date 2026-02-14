n, t = map(int, input().split())
moves = list(map(int, input().split()))

position = 1

while position < t:
    position += moves[position - 1]

if position == t:
    print("YES")
else:
    print("NO")