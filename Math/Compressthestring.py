from itertools import groupby

print(*[(len(list(i)), int(j)) for j, i in groupby(input())])