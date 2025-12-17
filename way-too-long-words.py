n = int(input())

for _ in range(n):
    w = input().strip()

    if len(w) > 10:
        first_letter = w[0]
        letters_between = len(w[1:-1])
        last_letter = w[-1]
        print(first_letter + str(letters_between) + last_letter)
    else:
        print(w)