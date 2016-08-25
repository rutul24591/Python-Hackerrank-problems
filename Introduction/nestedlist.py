n = int(input())
L=[]
for i in range(n):
    L.append([input(),float(input())])

second2lowest= sorted(list(set([marks for name,marks in L])))[1]
#try custom test case with 2 names and their respective marks which are same

#secondhighest.sort(reverse = True)
#print (second2lowest)
print('\n'.join([name for name,marks in sorted(L) if marks == second2lowest]))