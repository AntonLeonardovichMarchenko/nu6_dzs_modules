# Это смена рабочей директрии...

import os

# Модуль os предоставляет множество функций, которые можно применять при работе с операционной системой.
# Функция os.chdir даёт возможность сменить директорию.
# При запуске скрипта базовой папкой является та, в которой этот скрипт был запущен.
# Функция os.getcwd() позволяет узнать полный текущий путь к рабочей папке.

newDirectory = "C:\PythonDrom\Tests_2022\multithreading\stage_0"


def test():
    print('this is Change Working Directory')
    changeIt()


def changeIt():
    print(f"Текущая директория: {os.getcwd()}")
    print(newDirectory)
    os.chdir(newDirectory)  # смена директории
    print(f"Новая директория: {os.getcwd()}")
