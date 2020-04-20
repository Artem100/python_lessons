

first_task_list = [1, 2, 3, 4, 5, 6]
# password = input("*Задание 3*\nВведите пароль, который содержит больше 4-х символов, содержит только маленькие латинские число букв должно быть нечетным, а цифр четным: ")


def task_1(target_list, item_index1, item_index2):
   """Дан массив. Реализовать функцию которая будет переставлять 2 выбранных элемента списка местами"""
   print(f"Input target list: {target_list}")
   target_list[item_index1] , target_list[item_index2] = target_list[item_index2] , target_list[item_index1]
   print(f"Output target list: {target_list}")



def task_2():
   """Дан массив целых чисел. Нужно найти сумму элементов с индексами подходящими под правило.

   Правило такое - сумма бит двоичного представления четна.

   Затем перемножить эту сумму и предпоследний элемент исходного массива.
   """
   """ Что значит (сумма бит двоичного представления четна):
   1. Откуда брать эту сумму
   """

def task_3(password):
   """Дается строка - нужно проверить является ли она валидным паролем:

   - длина больше 4 символов,

   - содержит только маленькие латинские буквы и цифры,

   - число букв должно быть нечетным, а цифр четным."""
   lower_letters = 0
   list_digits = 0
   while lower_letters < 1 or list_digits < 1:
      if len(password) >= 4:
         # Проверяем длину пароля
         for i in password:
            #Делаем перебор символов в пароле
            if len(password) > 3:
               pass
            if i.isalpha():
               # Если это буква
               if i.islower():
                  # Если это маленькая буква, добавляет к счетчику букв 1
                  lower_letters += 1
                  continue
            elif i.isdigit():
            # Если это цифра, то добавляет к счетчику цифр 1
               list_digits += 1
               continue
            else:
               # Если пароль содержит большие буквы или другие символы
               password = input("Пароль дожен содержать только маленькие (латинские) буквы и цифры, попробуй еще раз: ")
         if lower_letters >= 1:
            # Проверяет нечетное ли количество букв в пароле
            if lower_letters % 2 != 0:
               pass
            else: password = input("Количество маленьких букв должно быть нечетным: ")
         else:
            # Проверяет четное ли количество цифр в пароле
            password = input("Пароль дожен содержать также и маленькие буквы попробуй еще раз: ")
         if list_digits >= 1:
            if list_digits % 2 == 0:
               pass
            else:
               password = input("Количество цифр должно быть четным: ")
         else:
            password = input("Пароль дожен содержать также и цифры еще раз: ")
      else:
         password = input("Пароль содержит меньше 4-х символов, попробуй еще раз: ")


def task_4():
   """Функция считывает значение прайс
   сравнивает его с текущим уже записанным значением
    - если больше, то записывает его в словарь как большее и отправляет весь товар наверх
    - если меньше то пусть продолжает
   """
   autos = [

      {"brand": "Ford", "model": "Mustang", "year": 1964, 'price': 4000},

      {"brand": "Ford", "model": "Mondeo", "year": 1999, 'price': 3000},

      {"brand": "Ford", "model": "Fiesta", "year": 2003, 'price': 4200},

      {"brand": "Nissan", "model": "Primera", "year": 1997, 'price': 3100},

      {"brand": "BMW", "model": "X3", "year": 2001, 'price': 5000},

      {"brand": "Nissan", "model": None, "year": 1964, 'price': None},

      {"brand": "VW", "model": "Passat", "year": 1996, 'price': 1200},

      {"brand": "BMW", "model": "X5", "year": 2010, 'price': 7500},

      {"brand": "Renault", "model": "Megane", "year": 1999, 'price': 2300},

   ]
   return print(sorted(autos, key=lambda x: x['price'], reverse=True))
   # Как быть с None


if __name__ == '__main__':
   # task_1(first_task_list, 0, 5)
   # task_3(password)g
   task_4()

