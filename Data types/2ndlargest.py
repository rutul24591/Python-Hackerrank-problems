a=int(input())
b= list(set(map(int, input().strip().split())))
b.sort(reverse= True)
print (b[1])