name = ['vishal', 'viraj', 'viabhav']

def get_prefix(name):
    if len(name) == 0:
        return 'list is empty'
    if len(name) == 1:
        return name[0]

    current_str = name[0]

    for i in range(1, len(name)):
        prefix = ''
        for j in range(len(name[i])):
            if j < len(current_str) and current_str[j] == name[i][j]:
                prefix = prefix + current_str[j]
            else:
                break
    return prefix

print(get_prefix(name))

