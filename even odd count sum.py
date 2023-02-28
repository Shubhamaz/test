# Count even and odd numbers from list

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def count_even_odd(lst):
    even = []
    odd = []

    for i in l1:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return f'even count: {len(even)} \nodd count: {len(odd)}'

print(count_even_odd(l1))


# program of count and print positive and negative numbers from list.

l2 = [-1, 2, -3, 4, 5, -6, 7, 8, -9, 10]

def count_positive_negetive(lst):
    p = []
    n = []
    for i in lst:
        if i < 1:
            p.append(i)
        else:
            n.append(i)
    return f'positive count: {len(p)} \nNegetive Count: {len(n)}'

print(count_positive_negetive(l2))


l3 = [1,2,3,4,5,6,7,8,9,10]

def sum_of_even_odd(l3):
    even_sum = 0
    odd_sum = 0
    for i in l3:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return f'even sum : {even_sum} \nodd sum: {odd_sum}'

print(sum_of_even_odd(l3))
