"""
#==========================================================================
Функция os.walk
Функция walk модуля os принимает один обязательный аргумент и несколько необязательных.
В качестве обязательного аргумента должен быть передан адрес каталога.

Функция walk() возвращает объект-генератор, из которого получают кортежи.
Каждый кортеж "описывает" очередной каталог из переданного в функцию дерева каталогов.

Каждый кортеж состоит из трех элементов:

Адрес очередного каталога в виде строки.
Список имен подкаталогов первого уровня вложенности в данный каталог.
Если вложенных каталогов нет, список будет пустым.
Список имен файлов первого уровня вложенности в данный каталог.
Если вложенных файлов нет, список будет пустым.

При передаче имени каталога "test" функции os.walk():

import os

tree = os.walk('test')
print(tree)

for i in tree:
    print(i)

<generator object walk at 0x7fa36d013740>
('test', ['cgi-bin'], ['index.html', 'dgs.png'])
('test/cgi-bin', ['another', 'backup'], ['hello.py'])
('test/cgi-bin/another', [], ['data.txt'])
('test/cgi-bin/backup', [], [])

Если передать абсолютный адрес, адреса каталогов также будут абсолютными:

import os

for i in os.walk('/home/pl/test'):
    print(i)

('/home/pl/test', ['cgi-bin'], ['index.html', 'dgs.png'])
('/home/pl/test/cgi-bin', ['another', 'backup'], ['hello.py'])
('/home/pl/test/cgi-bin/another', [], ['data.txt'])
('/home/pl/test/cgi-bin/backup', [], [])

Поскольку walk() возвращает генератор, повторно извлечь из него данные нельзя.
Поэтому, если возникает необходимость сохранить кортежи, генератор можно
"превратить" в список кортежей:

import os

tree = list(os.walk('test'))  # список кортежей

for i in tree:
    print(i)

('test', ['cgi-bin'], ['index.html', 'dgs.png'])
('test/cgi-bin', ['another', 'backup'], ['hello.py'])
('test/cgi-bin/another', [], ['data.txt'])
('test/cgi-bin/backup', [], [])

#========================================================================================

Чтобы получить полный адрес файла (абсолютный или относительный),
следует воспользоваться функцией os.path.join:

import os.path

for address, dirs, files in os.walk('test'):
    for name in files:
        print(os.path.join(address, name))

test/index.html
test/dgs.png
test/cgi-bin/hello.py
test/cgi-bin/another/data.txt

Переменная address на каждой итерации связывается с первым элементом очередного кортежа
                                                    (строкой, содержащей адрес каталога),
Переменная dirs – со вторым элементом (списком подкаталогов),
Переменная files - со списком файлов этого каталога.
Во вложенном цикле извлекается имя каждого файла из списка файлов.

#========================================================================================
"""






import os
from pathlib import Path


def test():
    print('this is See Only Folders')

    xcd = os.path.abspath(os.curdir)  # нашли текущую директорию в xcd её имя
    print()                           # это как C:\users\[имяюзера]

    i=0
    print(f'{i} : {xcd}')
    i+=1

    path = Path(xcd)


    DirectoryInfo=[]
    for address, dirs, files in os.walk(path):
        for name in dirs:
            #print(os.path.join(address, name))
            DirectoryInfo.append(os.path.join(address, name))

    for addressfolders in DirectoryInfo:
        print(f'{i} : {addressfolders}')
        i += 1

    return 1




