mystr = 'python automation'
d1 = {}
for i in mystr:
    if i in d1:
        d1[i] = d1.get(i) + 1
    else:
        d1[i] = 1

print(d1)