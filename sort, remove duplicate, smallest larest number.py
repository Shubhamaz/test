'''
1. remove duplicates
2. sort list
3. find smallest and largest number
'''


l3 = [1,2,4,5,8,1,2,3,6,5,4,10,123,10]

def Smallest_Largest_number(l3):
    removed_duplicate = []
    for i in l3:
        if i not in removed_duplicate:
            removed_duplicate.append(i)
    
    for i in removed_duplicate:
        for j in removed_duplicate:
            if i > j:
                i, j = j, i
    print(f'smallest number: {removed_duplicate[1]} \nlargest number: {removed_duplicate[-1]}')
    return removed_duplicate

print(Smallest_Largest_number(l3))


l1 = ['a', 'B', 's', 'w']

def sortl(l1):
    for i in l1:
        for j in l1:
            if ord(i) > ord(j):
                i, j = j, i
    return l1

print(sortl(l1))