lst = [1,2,3,4,5,6,7,8,9]

def check_two_sum(lst, target):
    l2 = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                l2.append([lst[i], lst[j]])
    return l2

print(check_two_sum(lst, 5))