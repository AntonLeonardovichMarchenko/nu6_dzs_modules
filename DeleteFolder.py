"""
Проверка наличия файла или каталога по указанному пути
=========================================================================================
Если надо проверить корректность введенного пользователем адреса файла или каталога,
сделать это можно с помощью функции os.path.exists, которая возвращает true,
если объект файловой системы существует, и false – если нет.

Функция os.path.isfile проверяет, является ли объект файлом,
      а os.path.isdir — является ли каталогом.

В приведенном ниже скрипте проверяется наличие объекта по указанному пользователем адресу,
после этого проверяется файл это или каталог.
В зависимости от типа объекта выводится информация.

# Скрипт проверяет наличие пути.
# Если файл, то выводит его размер, даты создания, открытия и модификации.

# Каталог !!!
# Если каталог, выводит список вложенных в него файлов и каталогов.

import os
import datetime

test_path = input('Введите адрес: ')

if os.path.exists(test_path):
    if os.path.isfile(test_path):
        print('ФАЙЛ')
        print('Размер:', os.path.getsize(test_path) // 1024, 'Кб')
        print('Дата создания:',
                  datetime.datetime.fromtimestamp(
                      int(os.path.getctime(test_path))))
        print('Дата последнего открытия:',
                  datetime.datetime.fromtimestamp(
                      int(os.path.getatime(test_path))))
        print('Дата последнего изменения:',
                  datetime.datetime.fromtimestamp(
                      int(os.path.getmtime(test_path))))
    elif os.path.isdir(test_path):
        print('КАТАЛОГ')
        print('Список объектов в нем: ', os.listdir(test_path))
    else:
        print('Объект не найден')

    В скрипте также используются функции os.path.getsize (возвращает размер файла),
    os.path.getctime (время создания), os.path.getatime (время последнего открытия),
    os.path.getmtime (дата последнего изменения).
    Метод datetime.datetime.fromtimestamp позволяет выводить время в местном формате.

    Примеры выполнения программы:

    Введите адрес: /home/pl/test.py
    ФАЙЛ
    Размер: 2 Кб
    Дата создания: 2021-10-14 19:55:58
    Дата последнего открытия: 2022-04-21 08:21:00
    Дата последнего изменения: 2021-10-14 19:55:58

    Введите адрес: /home/pl/pas
    КАТАЛОГ
    Список объектов в нем:  ['vk', 'theory', 'tasks']

"""

# Скрипт проверяет наличие пути.
# Если это путь файла, то выводится его размер, даты создания, открытия и модификации.
# Если это путь каталога, то выводится список вложенных в него файлов и каталогов.

import os
import shutil

def test():
    print('this is Delete Folder')
    ret = doIt()
    return ret

def doIt():

    deletedfolder = input('deleted Folder name: ')
    print(deletedfolder)

    path = os.getcwd()
    print(path)

    if os.path.isdir(path):
        print('КАТАЛОГ')
        print('Список объектов в нем: ', os.listdir(path))

    if os.path.exists(deletedfolder):
        print(f'Папка {deletedfolder} удаляется')
        shutil.rmtree(deletedfolder)

        return 1
    else:
        print(f'папка {deletedfolder} в каталоге {path} не найдена')

        return 0
