n = int(input())

solutions = 0

for _ in range(n):
    votes = list(map(int,input().split()))
    # input() → "1 0 1" (a single string)
    # split() → ["1", "0", "1"] (list of strings)
    # map(int, ...) → 1, 0, 1 <iterator> producing integers
    # list(...) → [1, 0, 1] (list of integers)
    consensus = 0
    for v in votes:
        if v:
            consensus += 1
    if consensus > 1:
        solutions += 1

print(solutions)