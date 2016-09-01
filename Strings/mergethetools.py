import textwrap
S = input()
K = int(input())

for a in textwrap.wrap(S, K):
    modified_a = ""
    for ch in a:
        if ch not in modified_a:
            modified_a += ch
    print(modified_a)