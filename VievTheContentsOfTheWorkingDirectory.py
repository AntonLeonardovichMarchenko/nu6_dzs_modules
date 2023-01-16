"""
Функция dir() в Python, все атрибуты объекта.
Возвращает список допустимых атрибутов объекта.
Синтаксис:
dir(object)
Параметры:
object - объект языка Python, для которого следует вернуть имена атрибутов.
Возвращаемое значение:
list - список имён (атрибутов) в алфавитном порядке.
Описание:
Функция dir(), вызванная без аргумента, возвращает список имен в текущей локальной области,
а вызванная с аргументом попытается вернуть список допустимых атрибутов для указанного объекта.
Если объект имеет метод с именем __dir__(), этот метод будет вызван и вернет список атрибутов.
Это позволяет объектам, реализующим пользовательскую функцию __getattr__() или __getattribute__(),
 настраивать способ представления своих атрибутов для функции dir().
Если объект не предоставляет метод __dir__(), то функция делает все возможное,
чтобы собрать информацию из атрибута __dict__ объекта, если он определен, и из объекта типа.
Результирующий список не обязательно является полным и может быть неточным,
если объект имеет пользовательский __getattr__().
Механизм dir() по умолчанию ведет себя по-разному с различными типами объектов,
поскольку он пытается создать наиболее релевантную, а не полную информацию:
Если объект является модулем, список будет содержать имена атрибутов модуля;
Если объект является типом или классом, список будет содержать имена атрибутов данного объекта
 и его родителей (вычисляются рекурсивно).
В других случаях список будет содержать имена атрибутов самого объекта, его класса,
и классов-родителей (вычисляются рекурсивно).
Функция dir() в основном используется в интерактивном режиме интерпретатора.
Она пытается предоставить интересный набор имен, а не строго определенный набор имен.
Ее поведение может изменяться в разных версиях Python.

Примеры получения списка атрибутов объекта.
x = 5
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__',
'__name__', '__package__', '__spec__', 'x']

import struct
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__',
'__name__', '__package__', '__spec__', 'struct', 'x']

dir(struct)
['Struct', '__all__', '__builtins__', '__cached__', '__doc__',
'__file__', '__loader__', '__name__', '__package__', '__spec__',
'_clearcache', 'calcsize', 'error', 'iter_unpack', 'pack', 'pack_into',
'unpack', 'unpack_from']
class Shape:
...     def __dir__(self):
...         return ['area', 'perimeter', 'location']
 s = Shape()
 dir(s)
['area', 'location', 'perimeter']

==========================================================================
import os    # путь к директории без названия файла
a = os.path.basename(__file__)
b = os.path.abspath(__file__).replace(a, '')
==========================================================================
Получить текущую директорию, где запущен скрипт
dir = os.path.abspath(os.curdir)

Получить текущую директорию, где расположен скрипт
os.path.abspath(__file__)
==========================================================================
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

У функции walk есть аргумент topdown, который по умолчанию имеет значение True.
Если ему присвоить False, то обход дерева каталогов будет происходить не "сверху вниз"
(от корневого к вложенным), а наоборот - "снизу вверх" (первыми будут подкаталоги).

import os

tree = os.walk('test', topdown=False)

for i in tree:
    print(i)
('test/cgi-bin/another', [], ['data.txt'])
('test/cgi-bin/backup', [], [])
('test/cgi-bin', ['another', 'backup'], ['hello.py'])
('test', ['cgi-bin'], ['index.html', 'dgs.png'])


"""

import os
from pathlib import Path

def test():
    print('this is View The Contents Of The Working Directory')

    xcd = os.path.abspath(os.curdir)  # нашли текущую директорию в xcd её имя
    path = Path(xcd)


    DirectoryInfo = []
    for row in os.walk(path):  # os.walk() обходит дерево каталогов и возвращает
                               # генератор!!! кортежей, каждый из которых содержит
                               # имя каталога, списки вложенных каталогов и файлов.
        for filename in row[2]:  # row[2] список файлов в каталоге
            full_path: Path = Path(row[0]) / Path(filename)  # row[0] имя каталога
            DirectoryInfo.append(full_path)
            #                   путь\имя_файла

    print(f'\n==============================================================\n')

    i = 0
    for member in DirectoryInfo:
        print(f'{i} : {member}')
        i+=1

    print(f'\n==============================================================\n')

    fmc = FileManagerContents('w', DirectoryInfo)
    fmc.fileManagerContentsForWrite()

    return 1

#========================================================================================

class FileManagerContents:

    DepotDirName = 'Depot'
    DepotFileName = 'contentDep.txt'

    fcp = None  #  file content path
    cf = None   #  content file

    DirectoryInfo = []


    def __init__(self, key, DirectoryInfo):
        # создаётся директория DepotDirName с файлом DepotFileName 'depot\contentDep.txt'
        # Здесь key всегда (пока!!!) равно 'w' а в DirectoryInfo вся собранная для
        # записи информация о рабочей директории ========================================

        FileManagerContents.DirectoryInfo = DirectoryInfo

        CurrentWD = os.getcwd()
        ContentPath = CurrentWD + '\\' + FileManagerContents.DepotDirName

        if os.path.exists(ContentPath) == False:
            print(f'~1~: {ContentPath} is not exist')
            os.mkdir(ContentPath)


        FileManagerContents.fcp = ContentPath + '\\' + FileManagerContents.DepotFileName
        FileManagerContents.cf = open(FileManagerContents.fcp, key)

    @classmethod
    def fileManagerContentsForWrite(cls):
        try:
            # открывается файл для записи инфы в рабочей директории 'contentDep.txt'
            FileManagerContents.cf.close()   # удаление старых записей
            FileManagerContents.cf = open(FileManagerContents.fcp, 'a')
                                             # открытие пустого файла
        # Ранее созданный файл открывается на запись как новый ==========================
        # список значений из DirectoryInfo пишется в 'contentDep.txt' ===================
            for value in FileManagerContents.DirectoryInfo:
                print(f'{value}')
                # запись стоки в 'contentDep.txt'
                stringContentsInfo = str(value) + '\n'
                FileManagerContents.cf.write(stringContentsInfo)
        finally:
            # после действий с FileManagerBanc файл для записи инфы
            # в рабочей директории 'contentDep.txt' закрывается
            # (запись ВСЕХ строк FileManagerContents.DirectoryInfo) файл закрывается
            FileManagerContents.fileContentAccountClose()

    # ===============================================================================

    @classmethod
    def fileContentAccountClose(cls):
        FileManagerContents.cf.close()
#========================================================================================



