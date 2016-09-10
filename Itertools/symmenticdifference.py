int(input())
M = set(map(int, input().split(" ")))
int(input())
N = set(map(int, input().split(" ")))

MDif = M.difference(N)
NDif = N.difference(M)
res = sorted(list(MDif)+list(NDif))

for i in res:
    print(i)