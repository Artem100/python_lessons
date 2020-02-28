import itertools
import os
import random
import string
import zipfile
from os.path import dirname, abspath
from time import strftime

from urllib3.util import current_time

z = zipfile.ZipFile('lesson6.zip', 'r')
file_name = "files_"+strftime("%I_%M%p")
err = None
for i in itertools.product(string.ascii_lowercase, repeat=3):
    try:
        print(''.join(i))
        z.extractall(file_name, pwd=''.join(i).encode('cp850', 'replace'))
        break
    except:
        #err = e
        continue
z.close()

"""
    1. Парсер чтобы создать по уникальному городу -> Внутри текстовый файл -> Внутри укникальные запросы (ключ слова) 
        - указать кол. уникальных юзеров  
"""