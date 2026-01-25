a = int(input())
b = int(input())
c = int(input())

answer = max(
    a + b + c,
    a * b * c,
    a + (b * c),
    (a + b) * c,
    (a * b) + c,
    a * (b + c)
)

print(answer)