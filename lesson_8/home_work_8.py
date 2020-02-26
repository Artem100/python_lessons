import itertools
import os
import random
import string
import zipfile
from os.path import dirname, abspath
from time import strftime

from urllib3.util import current_time

z = zipfile.ZipFile('lesson6.zip')
# file_name = "files_"+strftime("%I_%M%p")
# os.mkdir(file_name)
# count_files = len(os.listdir(file_name))

    for i in itertools.combinations_with_replacement(string.ascii_lowercase, 3):
        try:
            print(z.namelist())
            #print(''.join(i))
            #z.extractall(file_name, pwd=''.join(i).encode('cp850', 'replace'))
        except:
            continue
    break
z.close()