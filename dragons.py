s, dn = map( int, input().split() )

dragons = []

for _ in range(dn):
    ds, bs = map( int, input().split() )
    dragons.append( (ds, bs) )

dragons.sort()

for ds, bs in dragons:
    if s > ds:
        s += bs
    else:
        print("NO")
        exit()

print("YES")