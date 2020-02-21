import heapq
stud = [['KRIS', 54, 56, 90], ['ANA', 66, 77, 88]]
new_list = []
for i in stud:
    dict_stud = dict()
    sum = 0
    key = stud[0]
    for j in i:
        if type(j) is int:
            sum = sum + j
        else:
            key = j.split()
        all_list = dict_stud.fromkeys(key, sum)
    new_list.append(all_list)
print(new_list)

# heapq.nsmallest(0, li)
# print (list(li))