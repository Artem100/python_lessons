import string
from collections import Counter
from random import choice


def task_1():
    """Дана строка “spam and eggs or eggs with spam”. Посчитать сколько раз встретился каждый символ."""
    some_string = "spam and eggs or eggs with spam"
    #lis = [i for i in some_string]
    lis = list(some_string)
    print(Counter(lis))


def task_3():
    """На ввод подается строка. Нужно узнать является ли строка палиндромом."""
    any_string = input("Input any string for task 2: ")
    length = len(any_string)
    for i in range(length//2):
        if any_string[i] != any_string[-1-i]:
            print("It's not palindrome")
        else:
            print("It's palindrome")


def task_4():
    any_string = input("Input any string for task 4: ")
    word_List = any_string.split()
    inverted_list_words = []
    for i in word_List:
        inverted_list_words.append(i[::-1])
    inverted_string = ' '.join(inverted_list_words)
    print("Inverted string: "+inverted_string)


def task_5():
    length_of_password = input("Set length of password: ")
    string_of_symbols = string.ascii_letters+string.digits
    new_password = []
    if length_of_password != '0' and length_of_password.isdigit():
        for i in range(int(length_of_password)):
            new_password.append(choice(string_of_symbols))
        inverted_symbols = "".join(new_password)
        print(inverted_symbols)
    else:
        print("You enter non correct length value or set 0 length")

# task_1 = task_1()
# task_3 = task_3()
#task_4 = task_4()
task_5 = task_5()