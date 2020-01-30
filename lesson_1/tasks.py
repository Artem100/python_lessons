import collections
from collections import Counter

list = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13, 100]


def min_and_max_value_at_list(list=[]):
    max_index = list.index(max(list))
    max_value = max(list)
    min_index = list.index(min(list))
    min_value = max(list)
    print("Task 1")
    print("The minimum value in list (index:value) - ", min_index, ":", min_value)
    print("The maximum value in list (index:value) - ", max_index, ":", max_value)

def frequently_repeated_items(list=[]):
    # counter = Counter(list)
    # print(counter.keys())
    print(dict(Counter(list)))

def unique_values(list=[]):
    list_set = set(list)
    list_frozenset = frozenset(list)

    print(list_set)
    print(list_frozenset)




#feature_1 = min_and_max_value_at_list(list)
#feature_2=frequently_repeated_items(list)
feature_3=unique_values(list)