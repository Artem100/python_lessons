# while True:
#     i = int(input())
#     l = input().split(" ")
#
import string
from collections import deque

###Task 1
def task_1():
    """Есть список. Нужно реализовать операцию левый и правый сдвиг на указанный шаг.
    Нужно решение с deque и без него. Пример списка [1, 2, 3, 4, 5]  сдвиг влево на 4 для него даст [5, 1, 2, 3, 4]."""
    a = [1, 2, 3, 4, 5]
    d = deque(a)
    d.rotate(1)
    print("Сдвиг вправо с *deque*:", d)
    d.rotate(-1)
    print("Сдвиг влево вернет все обратно с *deque*:", d)
    a_new = a.append()[-1]
    print("Сдвиг вправо без deque: ", a)

###Task 2
def task_2():
    s = string.ascii_lowercase
    for i in range(0, len(s), 4):
        print(s[i:i+4])

# Task3
# LIST_STUDENTS = [['KRIS', 54, 56, 90], ['ANA', 66, 77, 88], ['JACK', 95, 50, 58]]
# ONE_STUD = ['KRIS', 54, 56, 90]
# sum = 0
# for int(i) in ONE_STUD:
#     if i.isdigit():
#         sum = i
#     else:
#         continue

#task_1 = task_1()
task_2 = task_2()