'''
Suppose following is string find the occurance of character in string without using built-in functions
my_string = "This is sample string"
Expected Output
{'T':1, 'h':1, 'i':3, 's':4, 'a':1, 'm':1, 'p':1,'l':1, 'e':1,'r':1, 'n'1, 'g':1}
'''

my_string = "This is sample string"

def count_char(str1):
    d1 = {}
    for i in str1:
        if i in d1:
            d1[i] = d1.get(i) + 1
        else:
            d1[i] = 1
    return d1

print(count_char(my_string))
    