def is_palindrome(num):
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    if rev == temp:
        return 'Palindrome Number'
    return 'Not Palindrome Number'



def Palindrome_in_range(num1, num2):
    for i in range(num1, num2+1):
        temp = i
        rev = 0

        while i > 0:
            d = i % 10
            rev = rev * 10 + d
            i //= 10
        if rev == temp:
            print(rev)



if __name__ == '__main__':
    print(is_palindrome(121))
    Palindrome_in_range(100, 500)