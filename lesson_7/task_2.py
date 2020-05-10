'''

2. Retry decorator

Предположим что у нам нужно скачать страничку из сети. Нужно реализовать декоратор, который будет делать указанное число попыток скачать страницу.

Страница для теста: https://httpbin.org/status/{status}

Коды ответа:

200 - Success

300 - Redirection

403, 404 - Client Errors

500 - Server Errors

1. Написать функцию которая будет делать запрос с указанным нами кодом ответа. Код ответа выбираем случайно из списка.
2. Сделать декоратор который будет обрабатывать коды ответа на запрос и если Х раз не удалось получить 200, то возвращать текст с ошибкой, иначе ОК.


'''
import random
import requests

CODES = [200, 300, 403, 404, 500]
URL = 'https://httpbin.org/status/{status}'

def dec_code(count_try):
    def create_reply(func):
        def wrapper():
            for i in range(count_try):
                print(func())
                if func() == 200:
                    return "Ok"
            return 'Error'
        return wrapper()
    return create_reply

@dec_code(3)
def request_1():
    code = random.choice(CODES)
    resp = requests.get(URL.format(status=code))
    return resp.status_code


if __name__ == '__main__':
    code_result = request_1
    print(code_result)


