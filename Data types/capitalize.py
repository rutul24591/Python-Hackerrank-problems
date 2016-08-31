# In One Line
# print(input().title())        Can't pass test case 3 with this code   I: 1 g 2 r 3g  O: 1 G 2 R 3G  EO: 1 G 2 R 3g
# Learn the difference between capitalize() and title()

print(" ".join((s.capitalize() for s in input().split(" "))))


# way 2 and a great one

# print(" ".join(s[0].upper()+s[1:] for s in input().split(' ')))