s1="e#fee"
s2="fe#fe"
s1.replace('#','f')
s2.replace('#','e')
counts=0
countf=0
for i in s1:
    if i=='s':
        counts+=1
    if i=='f':
        countf+=1

countss=0
countee=0
for j in s2:
    if j == 's':
        countss+=1
    if j == 'f':
        countee+=1
if counts == countss:
    print("MATCH")
else:
    print("DIFFERENT")