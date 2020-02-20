import string
from collections import Counter
from random import choice


def task_1():
    """Дана строка “spam and eggs or eggs with spam”. Посчитать сколько раз встретился каждый символ."""
    some_string = "spam and eggs or eggs with spam"
    lis = list(some_string)
    print(f"Задача 1.\nCounter(lis)")


def task_3():
    """На ввод подается строка. Нужно узнать является ли строка палиндромом."""
    any_string = input("Задача 3.\nВведите любое слово: ")
    length = len(any_string)
    for i in range(length//2):
        if any_string[i] != any_string[-1-i]:
            print("\nIt's not palindrome")
        else:
            print("\nIt's palindrome")


def task_4():
    """На ввод дается строка. Нужно каждое слово развернуть наоборот. Порядок слов не должен меняться."""
    any_string = input("Задача 4.\nВведите люое слово: ")
    word_List = any_string.split()
    inverted_list_words = []
    for i in word_List:
        inverted_list_words.append(i[::-1])
    inverted_string = ' '.join(inverted_list_words)
    print(f"Задача 4.\nРазвернутая строка: {inverted_string}")


def task_5():
    """Напишите генератор случайных паролей.
    После запуска программа должна ждать ввода числа - длины пароля и нажатия Enter.
    Завершить программу нужно если будет введен 0. Также нужно проверять является ли введенная строка числом.
    Допустимые символы - цифры, большие и маленькие латинские буквы.(нужно использовать метод input)"""

    length_of_password = input("Задача 5.\nВведите желаемую лину пароля: ")
    string_of_symbols = string.ascii_letters+string.digits
    new_password = []
    if length_of_password != '0' and length_of_password.isdigit():
        for i in range(int(length_of_password)):
            new_password.append(choice(string_of_symbols))
        inverted_symbols = "".join(new_password)
        print(f"Задача 5.\nНовый пароль:{inverted_symbols}")
    else:
        print("You enter non correct length value or set 0 length")

def task_6():
    """Дана строка "English = 78 Science = 83 Math = 68 History = 65". Вычислить сумму всех чисел в строке."""

    lessons_string = "English = 78 Science = 83 Math = 68 History = 65"
    lessons_list = lessons_string.split()
    sum = 0
    for i in lessons_list:
        if i.isdigit():
            sum = sum + int(i)
    print(f"Зачада 6.\nОбщая сумма: {sum}")


# task_1 = task_1()
# task_3 = task_3()
# task_4 = task_4()
# task_5 = task_5()
task_6 = task_6()