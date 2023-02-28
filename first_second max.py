l1 = [1,2,43,6,88,997,776,66,23]
first_max = l1[0]
second_max = l1[0]

for i in range(len(l1)):
    if l1[i] > first_max:
        first_max = l1[i]
for i in range(len(l1)):
    if l1[i] > second_max and l1[i] != first_max:
        second_max = l1[i]
print(first_max, second_max)
