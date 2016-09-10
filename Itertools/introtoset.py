N = int(input())
S = set(map(int,input().split(" ")))
print(sum(S)/len(S))    # take S instead of N because we need to use distinct heights and N does not provide that