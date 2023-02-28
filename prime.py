def isprime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return 'not a prime number'
        return 'Prime Number'
    return 'Not a Prime Number'


def prime_in_range(num1, num2):
    prime_number = []
    for i in range(num1, num2+1):
        if i > 1:
            for j in range(2, num1):
                if i % j == 0:
                    break
            else:
                prime_number.append(i)
    return prime_number
    

prime_numbers = [i for i in range(2, 21) if all(i % j != 0 for j in range(2, i))]

if __name__ == '__main__':
    print(isprime(3))
    print(isprime(7))
    print(isprime(8))
    print(isprime(15))
    print(prime_in_range(5, 20))
    print(prime_numbers)