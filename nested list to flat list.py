lst = [1,2,3,[4,[5,6,7,],8,[9]],10]

def flat_list(lst, res=[]):   
    for i in lst:
        if type(i) == list:
            flat_list(i)
        else:
           res.append(i) 
    return res

print(flat_list(lst))