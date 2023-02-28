l4 = [14,265,4,52,845,84,21,1,848]

large_ele = l4[0]
small_ele = l4[0]

for i in l4:
    if i > large_ele:
        large_ele = i
    else:
        small_ele = i

print(large_ele)
print(small_ele)