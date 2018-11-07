import os
import glob

for index, oldfile in enumerate(glob.glob("1.png"), start=1):
    newfile = '1.jpg'.format(index)
    os.rename (oldfile,newfile)