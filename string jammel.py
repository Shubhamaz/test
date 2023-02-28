s0 = "apple"
s1 = "ppela"

l1 = s0[0]
l2 = s1[0]

len_of_String = len(s0)

for i in range(len_of_String):
    l1.append(s0[i])
    l2.append(s1[i])

count = 0

for i in range(len_of_String):
    if l1[i] not in l2:
        count += 1
    
if count > 0:
    print('strings are not equal and not jumbled')
else:
    print('Strings are equal and jumbled')