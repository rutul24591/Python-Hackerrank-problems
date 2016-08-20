

#python 2
N = int(raw_input().strip())   # python 3      N = input()

if N % 2 == 0:
    if N > 20 or N > 1 and N <= 5:
        print("Not Weird")
    else:
        print("Weird")
else:
    print("Weird")