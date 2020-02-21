# while True:
#     i = int(input())
#     l = input().split(" ")
#
import string
from collections import deque

###Task 1
def task_1():
    print("\nЗадание 1")
    """Есть список. Нужно реализовать операцию левый и правый сдвиг на указанный шаг.
    Нужно решение с deque и без него. Пример списка [1, 2, 3, 4, 5]  сдвиг влево на 4 для него даст [5, 1, 2, 3, 4]."""
    a = [1, 2, 3, 4, 5]
    d = deque(a)
    d.rotate(1)
    print("Сдвиг вправо с *deque*:", d)
    d.rotate(-1)
    print("Сдвиг влево вернет все обратно с *deque*:", d)
    var = a.pop()
    a.insert(0, var)
    print("Обычный сдвиг вправо: ",a)
    var_2 = a.pop(0)
    a.append(var_2)
    print("Обычный сдвиг влево: ", a)

def task_2():
    print("\nЗадание 2")
    """2. Дана строка S. Нужно распечатать её подстроками длиной w. Например S=”ABCDEFGHIJKLIMNOQRSTUVWXYZ” и w=4 - выход
    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ"""
    w = 4
    s = string.ascii_uppercase
    print(f"Подстроки с длиной - {w}")
    for i in range(0, len(s), w):
        strings = s[i:i+4]
        print(strings)

def task_3():
    print("\nЗадание 3")
    """Дан список студентов.
    Каждая запись содержит имя студента, и его оценки по физике, математике и химии.
    Нужно сохранить данные в словарь и по вводимому имени выводить среднюю оценку по всем трем предметам.
    Пример - список
    [[‘Krishna’, 67, 68, 69], [‘Arjun’, 70, 98, 63], [‘Malika’, 52, 56, 60]].
    Если на вход придет имя Malika - ответ будет 56.00."""

    LIST_STUDENTS = [['KRIS', 54, 56, 90], ['ANA', 66, 77, 88], ['JACK', 95, 50, 58]]
    new_list = []
    for i in LIST_STUDENTS:
        dict_stud = dict()
        sum = 0
        key = LIST_STUDENTS[0]
        for j in i:
            if type(j) is int:
                sum = sum + j
            else:
                key = j.split()
            all_list = dict_stud.fromkeys(key, sum)
        new_list.append(all_list)
    print("Общий список учеников с оценками {Имя, оценка}: ", new_list)

def task_4():
    """Сортировать список от меньшего к большему с помощью *heapq* """
    # Не нашел как сортировать с помощью heapq


task_1 = task_1()
task_2 = task_2()
task_3 = task_3()