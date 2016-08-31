s = input()

vowels = 'AEIOU'

Kscore = 0
Sscore = 0

for i in range(len(s)):
    if s[i] in vowels:
        Kscore += (len(s)-i)
    else:
        Sscore += (len(s)-i)

if Kscore > Sscore:
    print("Kevin", Kscore)
elif Kscore < Sscore:
    print("Stuart", Sscore)
else:
    print("Draw")