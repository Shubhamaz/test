list1 = ['z', 'q', 't']
list2 = ['p', 'v', 'a', 't']

l3 = list1 + list2

def rearrange(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print(rearrange(l3))