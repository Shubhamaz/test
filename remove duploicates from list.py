numbers = [10,2,3,4,5,10,5,5,5]

sum = 0
for i in numbers:
    sum += i
print(sum)


n = [10,2,3,4,5,10,5,5,5]
result = []
s = [result.append(i) for i in n if i not in result]
print(result)
