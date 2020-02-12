

def compare_keys_2_1():
    a = {'a': 1, 'b': 4, 't': 67}
    b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
    keys_a = []
    keys_b = []
    for i in a:
        keys_a.append(i)
    for i in b:
        keys_b.append(i)
    result = list(set(keys_a) & set(keys_b))
    print("Task 2,1: ", result)

def compare_keys_2_2():
    a = {'a': 1, 'b': 4, 't': 67}
    b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
    keys_a = []
    keys_b = []
    final_keys = []
    for i in a:
        keys_a.append(i)
    for i in b:
        keys_b.append(i)

    for i in keys_b:
        if i != keys_a:
            final_keys.append(i)
    print(final_keys)




#compare_keys_2_1()
compare_keys_2_2()