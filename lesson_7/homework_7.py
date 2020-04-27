"""

HW 8 Decorators practice

1. mobile numbers

https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

Let's dive into decorators! You are given mobile numbers. Sort them in ascending order then print them in the standard format shown below:

+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual digit number. Alternatively, there may not be any prefix at all.

Input Format

The first line of input contains an integer, the number of mobile phone numbers.

lines follow each containing a mobile number.

Output Format

Print mobile numbers on separate lines in the required format.

Sample Input

3

07895462130

919875641230

9195969878

Sample Output

+91 78954 62130

+91 91959 69878

+91 98756 41230


2. Retry decorator

Предположим что у нам нужно скачать страничку из сети. Нужно реализовать декоратор, который будет делать указанное число попыток скачать страницу.

Страница для теста: https://httpbin.org/status/{status}

Коды ответа:

200 - Success

300 - Redirection

403, 404 - Client Errors

500 - Server Errors


    Написать функцию которая будет делать запрос с указанным нами кодом ответа. Код ответа выбираем случайно из списка.
    Сделать декоратор который будет обрабатывать коды ответа на запрос и если Х раз не удалось получить 200, то возвращать текст с ошибкой, иначе ОК.

"""