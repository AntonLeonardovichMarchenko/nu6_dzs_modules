"""

Как получить и изменить текущий рабочий каталог в Python

При работе с файлами в каталогах в Python всегда рекомендуется использовать абсолютные пути.
Однако, если вы работаете с относительными путями, необходимо понимать концепцию
текущего рабочего каталога и то, как найти или изменить текущий рабочий каталог.
Абсолютный путь указывает расположение файла или каталога, начиная с корневого каталога,
а относительный путь начинается с текущего рабочего каталога.

Когда запускается приложение Python, в качестве текущего рабочего каталога
устанавливается каталог, из которого выполняется сценарий.

Модуль os python обеспечивает переносимый способ взаимодействия с операционной системой.
Модуль является частью стандартной библиотеки Python и включает методы поиска и изменения
текущего рабочего каталога.

Получение текущего рабочего каталога в Python:
Метод getcwd() модуля os в Python возвращает строку, содержащую абсолютный путь
к текущему рабочему каталогу. Возвращенная строка НЕ включает завершающий символ косой черты.

os.getcwd()
Чтобы использовать методы модуля os, нужно импортировать модуль в верхней части файла.

Ниже приведен пример, показывающий, как распечатать текущий рабочий каталог:

# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
Результат будет выглядеть примерно так:

Если нужно найти каталог, в котором находится скрипт, надо применить
os.path.realpath(__file__) .
Он вернет строку, содержащую абсолютный путь к запущенному скрипту.


Изменение текущего рабочего каталога в Python:
Чтобы изменить текущий рабочий каталог в Python, надо использовать метод chdir() .

os.getcwd(path)
Метод принимает один аргумент — путь к каталогу, в который надо будет перейти.
Аргумент path может быть абсолютным или относительным.

Пример:

# Import the os module
import os

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory
os.chdir('/tmp')

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

Результат :

Current working directory: /home/linuxize/Desktop
Current working directory: /tmp
Аргумент, передаваемый методу chdir() должен быть каталогом,
в противном случае NotADirectoryError исключение NotADirectoryError .
Если указанный каталог не существует, возникает исключение FileNotFoundError.
Если у пользователя, от имени которого выполняется сценарий,
нет необходимых разрешений, возникает исключение PermissionError .

# Import the os module
import os

path = '/var/www'

try:
    os.chdir(path)
    print("Current working directory: {0}".format(os.getcwd()))
except FileNotFoundError:
    print("Directory: {0} does not exist".format(path))
except NotADirectoryError:
    print("{0} is not a directory".format(path))
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))

"""
import os

def test():
    print('this is Create Folder')
    ret = doIt()
    return ret


def doIt():

    path = os.getcwd()
    print(path)

    if os.path.isdir(path):

        createdFolderName = input('created Folder name: ')
        print(f'В каталоге {path} будет создана папка {createdFolderName}')
        resultPath = path + '\\' + createdFolderName

        try:
            os.mkdir(resultPath)
        except OSError as error:
            print(error)
            return 0

        print(f'Папка {createdFolderName} успешно размещена в каталоге {path}')
        print(f'{resultPath}')
        return 1
    else:
        print(f'КАТАЛОГ {path} не найден')
        return 0
