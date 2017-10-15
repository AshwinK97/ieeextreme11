import math

def bigfact(i, j):
    if i == j:
        return 1
    return (i * bigfact(i-1, j)) % (10**9 + 7)

def ifact(n):
    x = 1
    li = list(range(2, n + 1))
    for each in li:
        x = (x * each) % (10**9 + 7)
    return x

n = int(input())
values = [] # ai, bi, ci
for i in range(0, n):
    values.append(map(int, raw_input().split()))

#for v in values:
#    print (v[0] ** ( bigfact(v[1], v[2]) / bigfact(v[1]-v[2], 0) )) % (10**9 + 7)

print ifact(500000)
