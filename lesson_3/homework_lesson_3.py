# while True:
#     i = int(input())
#     l = input().split(" ")
#
import string
from collections import deque

###Task 1
def task_1():
    # Без deque использовать срезы?
    """Есть список. Нужно реализовать операцию левый и правый сдвиг на указанный шаг.
    Нужно решение с deque и без него. Пример списка [1, 2, 3, 4, 5]  сдвиг влево на 4 для него даст [5, 1, 2, 3, 4]."""
    a = [1, 2, 3, 4, 5]
    d = deque(a)
    d.rotate(1)
    #print("Сдвиг вправо с *deque*:", d)
    d.rotate(-1)
    #print("Сдвиг влево вернет все обратно с *deque*:", d)
    var = a.pop()
    a.insert(0, var)
    print(a)
    var_2 = a.pop(0)
    a.append(var_2)
    print(a)
    # a_new = a.append()[-1]
    # print("Сдвиг вправо без deque: ", a)

###Task 2
def task_2():
    """2. Дана строка S. Нужно распечатать её подстроками длиной w. Например S=”ABCDEFGHIJKLIMNOQRSTUVWXYZ” и w=4 - выход
    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ"""

    s = string.ascii_lowercase
    for i in range(0, len(s), 4):
        print(s[i:i+4])

def task_3():
    """Дан список студентов.
    Каждая запись содержит имя студента, и его оценки по физике, математике и химии.
    Нужно сохранить данные в словарь и по вводимому имени выводить среднюю оценку по всем трем предметам.
    Пример - список
    [[‘Krishna’, 67, 68, 69], [‘Arjun’, 70, 98, 63], [‘Malika’, 52, 56, 60]].
    Если на вход придет имя Malika - ответ будет 56.00."""

    """
    1. Цикл который будет создавать новый словарь
    1.1 Если это не цифра, просто добавлять в словарь
    1.2 Если цифра то добавлять в новую переменную и сумировать ее значение
    1.3 В конце подсчитывать общую оценку ученика
    2. Вывести ОТДЕЛЬНЫЙ СЛОВАРЬ КАЖДОГО УЧЕНИКА и его средний бал    
    """


    LIST_STUDENTS = [['KRIS', 54, 56, 90], ['ANA', 66, 77, 88], ['JACK', 95, 50, 58]]
    ONE_STUD = ['KRIS', 54, 56, 90]
    LIST_WITH_MIDDLE_MARK = []
    COMMON_LIST = []
    for i in LIST_STUDENTS:

        sum = 0
        for j in i:
            if type(j) is int:
                sum = sum + j
            else:
                LIST_WITH_MIDDLE_MARK.append(j)
        LIST_WITH_MIDDLE_MARK.append(sum)

    COMMON_LIST += LIST_WITH_MIDDLE_MARK
    print("Общий список учени: Имя, оценка: ", COMMON_LIST)

def task_4():
    """Сортировать список от меньшего к большему с помощью *heapq* """


# task_1 = task_1()
# # #task_2 = task_2()
task_3 = task_3()