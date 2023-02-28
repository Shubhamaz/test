l1 = [1,2,3,4,5,6,7,8,9,10]

def addition(lst):
    sum = 0
    for i in l1:
        sum += i
    return sum

def substration(lst):
    total = 0
    for i in l1:
        total -= i
    return total

def multiplication(lst):
    multi = 1
    for i in l1:
        multi *= i
    return multi

def factorial_of_each_ele(lst):
    res = [] 
    for i in lst:
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        res.append(fact)
    return res

if __name__ == '__main__':
    print('addition: ', addition(l1))
    print('substraction: ', substration(l1))
    print('multiplication: ', multiplication(l1))
    print('factorial_of_each_ele: \n', factorial_of_each_ele(l1))

