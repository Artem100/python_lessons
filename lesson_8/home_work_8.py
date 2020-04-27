import itertools
import os
import random
import string
import zipfile
from os.path import dirname, abspath
from time import strftime

from urllib3.util import current_time

"""
3. Распаковать (в итоге получится группа папок с файлами логов в таком формате)


 “device\tage\tsex\tcity\tuser_id\tsearch_keyword\tdomain\turl\ttype”


4. Создать папку и в ней для каждого города который встретится в логах, создать файл (вида “new_jersey.tsv”) в котором вывести все поисковые запросы и количество уникальных user_id с которыми они встречались (через \t)

  

alabama.tsv

   facebook\t23

   youtube\t13

   facebook login\t6

   ebay\t6

"""




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