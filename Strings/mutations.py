N = input()

V = input().split(" ")

L = list(N)

swap = V[0]

a= V[1]

L[int(swap)] = a

N = "".join(L)

print (N)