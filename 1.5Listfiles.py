import os
from os import *



def listing(katalog):
    print(katalog)

    element_list = os.listdir(katalog)

    for element in element_list:
        full_path = os.path.join(katalog, element)

        if os.path.isdir(full_path):
            listing(full_path)
        else:
            print(full_path)


listing(getcwd()) # path to my folder