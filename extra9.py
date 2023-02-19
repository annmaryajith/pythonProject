list1 = [1, 2, 3, 4, 5]
first_ele = list1[0]
last_ele = list1[-1]
list1[0] = last_ele
list1[-1] = first_ele
print(list1)