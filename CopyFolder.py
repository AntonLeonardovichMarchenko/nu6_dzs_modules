"""
While shutil.copy() will copy a single file, shutil.copytree() will copy
an entire folder and every folder and file contained in it.
Calling shutil.copytree(source, destination) will copy the folder at the path source,
along with all of its files and subfolders, to the folder at the path destination.
The source and destination parameters are both strings.
The function returns a string of the path of the copied folder.

The shutil.copytree() call creates a new folder named spam_backup
with the same content as the original spam folder.
You have now safely backed up your precious, precious spam.

"""


import shutil
import os
from pathlib import Path


def test():
    print('this is Copy Folder')
    copyfolder()
    return 1

def copyfolder():
    p = Path.home()
    print(f'{p}')
    newP= shutil.copytree(p / 'venv', p / 'venv_backup')
    print(f'{newP}')
