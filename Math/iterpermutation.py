from itertools import permutations

A = list(input().split(" "))
B = list(permutations(A[0],int(A[1])))

for i in sorted(B):
    print("".join(i))