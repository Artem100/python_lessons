def test_1():

    some_list = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 9, 9]

    count = []
    result = []
    i_max = (-1, -1)
    for i in range(len(some_list)-1):
        if some_list[i] == some_list[i+1]:
            count.append(some_list[i])
        else:
            result.append((some_list[i], len(count)+1))
            count = []
    if not count:
        result.append((some_list[-1], 1))
        #result.append(1)
    else:
        result.append((some_list[-1], len(count) + 1))
    for i in result:
        if i[1] > i_max[1]:
            i_max = i
    print(f"Максимальная последовательность {i_max}")

    print(count)
    print(result)

first = test_1()