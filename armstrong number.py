def isarmstrong(num):
    temp = num
    total = 0
    l = len(str(num))

    while num != 0:
        digit = num % 10
        total += digit ** l
        num //= 10

    if temp == total:
        return 'armstrong Number'
    return 'Not a armstrong Number'

print(isarmstrong(153))

def armstrong_in_range(n1, n2):
    for num in range(n1, n2+1):
        total = 0
        order = len(str(num))
        temp = num
        while temp > 0:
            digit = temp % 10
            total += digit ** order
            temp //= 10
        if num == total:
            print(num)



print(armstrong_in_range(100, 10000))