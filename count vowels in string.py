name = 'shubham zambare'

def is_vowel(ele):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if ele in vowels:
        return True
    return False

def get_vovel_count(user_input):
    d1 = {}
    for i in user_input:
        if is_vowel(i):
            if i in d1:
                d1[i] = d1.get(i) + 1
            else:
                d1[i] = 1
    return d1

print(get_vovel_count(name))