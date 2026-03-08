n, m = map(int, input().split())

# Minimal moves ignoring the multiple condition
k_min = (n + 1) // 2

# Find the smallest k >= k_min and k % m == 0
k = k_min
while k <= n:
    if k % m == 0:
        print(k)
        break
    k += 1
else:
    print(-1)