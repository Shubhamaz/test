'''
lambda:
    lambda is small annonymous function which can have number parameter but can have only one argument.

map :
    map applies the given function to each item of iterable and returns the result

filter:
    filter applies the given function to each item of an iterable 
    and returns the result for which only the function returns True

Reduce:
    reduce is a function that impliment mathematcal technique called folding or reduction.
    it applies given function to all items of iterable and return single cumulative value
'''  


# lambda
is_even = lambda a: 'True' if a % 2 == 0 else 'False'
print(is_even(2))


# map
numbers = list(map(lambda a: a % 2 == 0, [1,2,3,4,6,7,8,910]))
print(numbers)

# filter
check_len = list(map(len, ['python', 'django', 'html', 'css', 'javascript']))
print(check_len)

# reduce
from functools import reduce

addition = reduce(lambda a, b: a+b, [1,2,3,4])
print(addition)


def multi(n1, n2):
    return n1* n2

m = reduce(multi, [1,2,3,4])
print(m)

