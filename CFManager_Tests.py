"""
Переписать программу и проверить, правильно ли она работает.
Что для этого надо сделать? Можно запустить её несколько раз с различными
входными данными и убедиться в правильности выдаваемого ответа.
Но если это делать несколько раз? После каждого изменения?
Запускать ещё несколько раз? А если потом снова что-то поменяется?
Возможна ли автоматизация тестирования? Возможна (!).
В Python встроен модуль unittest (ИСПОЛНИТЕЛЬ ТЕСТА), который поддерживает
- автоматизацию тестов,
- использование общего кода для настройки и завершения тестов,
- объединение тестов в группы,
- отделение тестов от фреймворка для вывода информации.
Модуль unittest предоставляет богатый набор инструментов для написания и запуска тестов.
Однако достаточно лишь некоторых из них, чтобы удовлетворить потребности
большинства пользователей.

Для автоматизации тестов модуль unittest поддерживает некоторые важные концепции:
- Испытательный стенд (test fixture) - выполняется подготовка,
необходимая для выполнения тестов и все необходимые действия для очистки после выполнения
тестов. Это может включать, например, создание временных баз данных или запуск серверного
процесса.
- Тестовый случай (test case) - минимальный блок тестирования.
Он проверяет ответы для разных наборов данных. Модуль unittest предоставляет базовый класс
TestCase, который можно использовать для создания новых тестовых случаев.
- Набор тестов (test suite) - несколько тестовых случаев, наборов тестов или
и того и другого. Он используется для объединения тестов, которые должны быть
выполнены вместе.
- Исполнитель тестов (test runner) - компонент, который управляет выполнением тестов
и предоставляет пользователю результат. Исполнитель может использовать графический или
текстовый интерфейс или возвращать специальное значение, которое сообщает о результатах
выполнения тестов.

в StringTester скрипт для тестирования трех методов строк.
Тестовый случай создаётся путём наследования от unittest.TestCase.
3 отдельных теста определяются с помощью методов, имя которых начинается на test.
Это соглашение говорит исполнителю тестов о том, какие методы являются тестами.

Суть каждого теста
- вызов assertEqual() для проверки ожидаемого результата;
- вызов assertTrue() или assertFalse() для проверки условия;
- вызов assertRaises() для проверки, что метод порождает исключение.
Эти методы используются вместо обычного assert для того, чтобы исполнитель тестов
смог взять все результаты и оформить отчёт.

Методы setUp() и tearDown() (которые в данном простом случае не нужны)
позволяют определять инструкции, выполняемые перед и после каждого теста, соответственно.

Последние 2 строки показывают простой способ запуска тестов.
unittest.main() предоставляет интерфейс командной строки для тестирования программы.
При запуске из командной строки, этот скрипт выводит отчёт.

Интерфейс командной строки
unittest может быть использован из командной строки для запуска модулей с тестами,
классов или даже отдельных методов:

python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method

Можно также указывать путь к файлу:

python -m unittest tests/test_something.py

С помощью флага -v можно получить более детальный отчёт:

python -m unittest -v test_module
Для примера со строками подробный отчёт будет таким:

test_isupper (__main__.TestStringMethods) ... ok
test_split (__main__.TestStringMethods) ... ok
test_upper (__main__.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
-b (--buffer) - вывод программы при провале теста будет показан, а не скрыт, как обычно.
-c (--catch) - Ctrl+C во время выполнения теста ожидает завершения текущего теста
 и затем сообщает результаты на данный момент.
 Второе нажатие Ctrl+C вызывает обычное исключение KeyboardInterrupt.

-f (--failfast) - выход после первого же неудачного теста.

--locals (начиная с Python 3.5) - показывать локальные переменные для провалившихся тестов.

Обнаружение тестов
unittest поддерживает простое обнаружение тестов.
Для совместимости с обнаружением тестов, все файлы тестов должны быть модулями
или пакетами, импортируемыми из директории верхнего уровня проекта
(см. подробнее о правилах наименования модулей ).

Обнаружение тестов реализовано в TestLoader.discover(),
но может быть использовано из командной строки:

cd project_directory
python -m unittest discover
-v (--verbose) - подробный вывод.
-s (--start-directory) directory_name - директория начала обнаружения тестов
   (по умолчанию текущая).
-p (--pattern) pattern - шаблон названия файлов с тестами (по умолчанию test*.py).
-t (--top-level-directory) directory_name - директория верхнего уровня проекта
   (по умолчанию равна start-directory).

Организация тестового кода
Базовые блоки тестирования это тестовые случаи - простые случаи,
которые должны быть проверены на корректность.

Тестовый случай создаётся путём наследования от unittest.TestCase.

Тестирующий код должен быть самостоятельным (!), то есть никак (!)
не зависеть от других тестов.

Простейший подкласс TestCase может просто реализовывать тестовый метод
(метод, начинающийся с test). Вымышленный пример:

import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

То есть, для того, чтобы проверить что-то, используется один из assert\*() методов.

Тестов может быть много, и часть кода настройки может повторяться.
Но можно определить код настройки путём реализации метода setUp(),
который будет запускаться перед каждым тестом (и это хорошо):

import unittest

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

Также можно определить метод tearDown(), который будет запускаться после каждого теста:

import unittest

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

Можно разместить все тесты в том же файле, что и сама программа
(таком как widgets.py), но размещение тестов в отдельном файле
(таком как test_widget.py) имеет много преимуществ:

- Модуль с тестом может быть запущен автономно из командной строки.
- Тестовый код может быть легко отделён от программы.
- Меньше "искушения" изменить тесты для соответствия коду программы
  без видимой причины.
- Тестовый код должен изменяться гораздо реже, чем программа.
- Протестированный код может быть легче переработан.
- Тесты для модулей на C должны быть в отдельных модулях,
  так почему же не быть последовательным? (точно...)
- Если стратегия тестирования изменяется, нет необходимости изменения кода программы.


"""





from tkinter import *

import sys
import os
import math

import BancAccount
import CreateFolder
import DeleteFile
import DeleteFolder
import CopyFolder
import CopyFile
import ViewTheContentsOfTheWorkingDirectory
import SeeOnlyFolders
import SeeOnlyFiles
import SeeOperationSystemInformation
import ProgramCreator
import Quiz
import ChangeWorkingDirectory

import numpy as np
import array as arr
import unittest

import shutil
from my_sum import sum




# Источник: https: // pythononline.ru / osnovy / kopirovat - fayl - python?ysclid = lclp3l72q5186082059



from pathlib import Path

# При написании и исполнении тестов unittest нужно соблюдать некоторые важные требования.
#  Нужно:
#
# - Помещать тесты в классы, как методы;
# - Использовать специальные методы утверждения.
#   Класс TestCase вместо обычного встроенного выражения assert.
#
# Чтобы превратить ранее написанный пример в тест-кейс unittest, необходимо:
#
# = Импортировать unittest из стандартной библиотеки;
# = Создать класс под названием TestSum, который будет наследовать класс TestCase;
# = Сконвертировать тестовые функции в методы, добавив self в качестве первого аргумента;
# = Изменить утверждения, добавив использование self.assertEqual() метода в классе TestCase;
# = Изменить точку входа в командной строке на вызов unittest.main().


class TestStringMethods(unittest.TestCase):

    def test_default_widget_size(self):
        try:
            self.assertEqual(50, 50)
            print(f'the first test is OK')
        except self.failureException as msg:
            print(f'{msg}')


    def test_upper(self):
        try:
            self.assertEqual('go go'.upper(), 'GO GO')
            print(f'the second test is OK')
        except self.failureException as msg:
            print(f'{msg}')

    def test_isupper(self):
        try:
            self.assertTrue('GO GO'.isupper())
            self.assertFalse('Go go'.isupper())
            print(f'the third test is OK')
        except self.failureException as msg:
            print(f'{msg}')

    def test_split(self):
        s = 'hello world'
        try:
            self.assertEqual(s.split(), ['hello', 'world'])
            # Проверка того, что s.split НЕ работает,
            # если разделитель - НЕ строка
            with self.assertRaises(TypeError):
                s.split(2)
            print(f'the fourth test is OK')
        except self.failureException as msg:
            print(f'{msg}')

    def test_files_copy(self, txt_srcFile, txt_targFile):

        try:
            #==================================================================
            file1 = input(f'{txt_srcFile} file: ')
            src_file_obj = open(file1, 'rb')  # не найден srcFile
            file2 = input(f'{txt_targFile} file: ')
            targ_file_obj = open(file2, 'wb')
            shutil.copyfileobj(src_file_obj, targ_file_obj)
            size1 = os.path.getsize(file1)
            targ_file_obj.close()
            size2 = os.path.getsize(file2)
            self.assertEqual(size1, size2)  # в результате копирования srcFile -> targFile
                                            # некорректное копирование
                                            # файлы разной длины (???).

            print(f'the five test is OK')   # результат тестирования OK,
            # если при выполнении кода в блоке try не случилось исключений.
            #============================================================================

        except FileNotFoundError as err:  # не найден исходный файл...
            #============================================================================
            sss = err.strerror + ' ' + err.filename
            print(f'{sss}')
            print(f'the five test is NOT OK')
            #============================================================================

        except self.failureException as msg:  # некорректное копирование
            #============================================================================
            print(f'{msg}')    # в том числе, файлы разной длины
            #============================================================================



class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        try:
            self.assertEqual(result, 6)
            print(f'test_list_int is OK')
        except Exception as ex:  #   ^
            print(f'{ex}')       #   |
            print(f'test_list_int is not OK')
        # возвращаемое значение      |
        # sum со значениями          |
        # аргумента data             |
        # должна быть равна          |
        # вот этому значению.--------+
        # И это равенство проверяется
        # тестирующей функцией assertEqual,
        # объявленной в unittest.TestCase.



    def test_list_int_2(self, data, testValue):
        """
        Test that it can sum a list of integers
        """

        result = sum(data)

        try:
            self.assertEqual(result, testValue)
            print(f'test_list_int_2 is OK')
        except Exception as ex:
            print(f'!!! {ex} !!!')
            print(f'test_list_int_2 is not OK')

    def test_pi(self, pi, *tstArr):

        try:
            #self.assertIn(pi, tstArr) # assertIn НЕ НАХОДИТ pi в интервале [3.0, 4.0]...
            # грёбаная железяка! Здесь приходится делать через задницу.
            self.assertTrue(pi >= tstArr[0] and pi <= tstArr[1])
            #self.assertTrue(inArr)
            print(f'test_pi is OK')
        except Exception as ex:
            print(f'!!! {ex} !!!')
            print(f'test_pi is not OK')

# модуль, содержащий тесты загружается первым. При этом значение переменной
# __name__ == имени модуля (то есть, CFManager_test).
# Интерпретатор старается выполнить его в первую очередь и на этом завершить выполнение
# ВСЕЙ программы. Чтобы предотвратить такой сценарий выполнения программы, и не допустить
# несвоевременного его выполнения, для загрузки этого модуля в модуле main применяется
# дополнительный параметр, при котором выполняется условие
# if __name__ == '__main__':.

# unittest.main()  # здесь большой список параметров!
# И (мне) пока непонятно, как его настраивать. Тем более,
# вся эта хрень запускается через обычную main.
# А уже в ней создаются тестовые объекты, через которые
# запускаются функции тестирования.

def main():

    tsm=TestStringMethods()

    # тесты вызываются в результаете обращения
    # к объекту tsm класса TestStringMethods.
    # В нём определены разнообразные тесты.
    # По сравнению с описанием в разных статьях
    # получилось не совсем так...

    tsm.test_default_widget_size()
    tsm.test_upper()
    tsm.test_isupper()
    tsm.test_split()

    # тест на корректное копирование файлов.
    # Тексты приглашений для проверки возможности передачи
    # параметров (строки) в тест.
    txt_srcFile = input(f'invitation text for find end open src file: ')
    txt_targFile = input(f'invitation text for open or create targ file: ')

    tsm.test_files_copy(txt_srcFile, txt_targFile)
    #          параметры:     строки приглашений



    tstSum = TestSum()

    tstSum.test_list_int()
    # в этом тесте параметры задаются непосредственно при объявлении
    # тестирующей функции (она поэтому без параметров)

    data = [1, 2, 3]

    testValue = 99
    tstSum.test_list_int_2(data, testValue)
    # а эта тестирующая функция с параметрами.
    # То есть, в этом тесте параметры задаются при ВЫПОЛНЕНИИ

    testValue = 6
    tstSum.test_list_int_2(data, testValue)

    print(f'===== test_pi [13.0, 14.0] =====')
    tstSum.test_pi(math.pi, *np.array([13.0, 14.0]))
    print(f'===== test_pi [3.0, 4.0] =====')
    tstSum.test_pi(math.pi, *np.array([3.0, 4.0]))

    print(f'the end of CFManager_Tests')

if __name__ == '__main__':
    main()






