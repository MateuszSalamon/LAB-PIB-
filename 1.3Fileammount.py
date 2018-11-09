import os
from os import *

dir = getcwd() # my dir, because i can't find /dev dir
list = os.listdir(dir)
number_files = len(list)
print(number_files, "files in dir")
