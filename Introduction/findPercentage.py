N = int(input())
dict = {}
for i in range(N):
    a = input().split(" ")
    # print(a)
    grades = list(map(float, a[1:]))
    dict[a[0]] = sum(grades) / len(grades)

print("%.2f" % round(dict[input()], 2))
