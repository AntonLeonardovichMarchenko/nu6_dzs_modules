"""
1. Создать новый проект "Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:

- создать папку;
- удалить папку;
- удалить файл;
- копировать папку;
- копировать файл;
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.

Так же можно добавить любой дополнительный функционал по желанию.
Описание пунктов:

- создать папку > после выбора пользователь вводит название папки,
                                    создаем её в рабочей директории;

- удалить папку > после выбора пользователь вводит название папки,
                  удаляем из рабочей директории если такой есть;

- удалить файл > после выбора пользователь вводит название файла,
                 удаляем из рабочей директории если такой есть;

- копировать папку > после выбора пользователь вводит название папки
                            и новое название папки. Копируем;

- копировать файл > после выбора пользователь вводит название файла
                                                и новое название файла. Копируем;

- просмотр содержимого рабочей директории > вывод всех объектов в рабочей папке;

- посмотреть только папки > вывод только папок которые находятся в рабочей папке;

- посмотреть только файлы > вывод только файлов которые находятся в рабочей папке;

- просмотр информации об операционной системе > вывести информацию об операционной системе
                                                (можно использовать пример из 1-го урока);

- создатель программы > вывод информации о создателе программы;

- играть в викторину > запуск игры викторина из предыдущего дз;

- мой банковский счет > запуск программы для работы с банковским счетом из предыдущего дз (???)
                        (задание учебное, после выхода из программы управлением счетом в
                        главной программе сумму и историю покупок можно не запоминать);

- смена рабочей директории (*необязательный пункт) > усложненное задание пользователь
                                                     вводит полный /home/user/...
                                                     или относительный user/my/... путь.
                                                     Меняем рабочую директорию на ту,
                                                     что ввели и работаем уже в ней;

- выход > выход из программы.

Так же можно добавить любой другой интересный или полезный функционал по своему желанию
(желания нет)
После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь
не выберет выход
3. Выложить проект на github.
4. Можно сдать задание в виде pull request.
5. Посмотреть разбор дз по функциям, если требуется, то сделать работу надо ошибками.
                                                                          (ха-ха-ха)


"""

# ========================================================================
from tkinter import *

import sys

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

import CFManager_Tests

import runpy

import Exit

"""
Последовательность действий при создании GUI-программы:
1. ! Создать главное окно!
2. Создать виджеты и выполнить конфигурацию их свойств (опций).
3. Определить события - то, на что будет реагировать программа.
4. Описать обработчики событий - то, как будет реагировать программа.
5. Расположить виджеты в главном окне.
6. ! Запустить цикл обработки событий!
Последовательность действий 2 - 5 не обязательно именно такая, 
НО пункты 1 и 6 ВСЕГДА остаются на своих местах.

"""

class CFManager:

    def __init__(self, funName ):
        self.masterRoot = Tk()    # приложение заключается в окно, которое называтся главным,
                                  # так как в нем располагаются все остальные виджеты.
                                  # Это объект окна верхнего уровня. Этот объект создается от
                                  # класса Tk модуля tkinter. Переменная, которая связывается
                                  # с объектом, часто называется root (корень).
        self.var = IntVar()
        self.var.set(0)

        self.rbCreateFolder = Radiobutton(text="create folder", variable=self.var, value=0)
        self.rbCreateFolder.pack() #"create folder"

        self.rbDeleteFolder = Radiobutton(text="delete folder", variable=self.var, value=1)
        self.rbDeleteFolder.pack() #"delete folder"
        self.rbDeleteFile = Radiobutton(text="delete file", variable=self.var, value=2)
        self.rbDeleteFile.pack() # "delete file"
        self.rbCCopyFolder = Radiobutton(text="copy folder", variable=self.var, value=3)
        self.rbCCopyFolder.pack() #"copy folder"
        self.rbCopyFile = Radiobutton(text="copy file", variable=self.var, value=4)
        self.rbCopyFile.pack() #"copy file"

        self.rbViewTheContentsOfTheWorkingDirectory = Radiobutton(text="view the contents of the working directory",
                                                                  variable=self.var, value=5)
        self.rbViewTheContentsOfTheWorkingDirectory.pack() #"view the contents of the working directory"

        self.rbSeeOnlyFolders = Radiobutton(text="see only folders", variable=self.var, value=6)
        self.rbSeeOnlyFolders.pack() #"see only folders"
        self.rbSeeOnlyFiles = Radiobutton(text="see only files", variable=self.var, value=7)
        self.rbSeeOnlyFiles.pack() #"see only files"

        self.rbSeeOperationSystemInformation = Radiobutton(text="see operation system information",
                                                           variable=self.var, value=8)
        self.rbSeeOperationSystemInformation.pack() #"see operation system information"

        self.rbProgramCreator = Radiobutton(text="program creator", variable=self.var, value=9)
        self.rbProgramCreator.pack() #"program creator"

        self.rbQuiz = Radiobutton(text="quiz", variable=self.var, value=10)
        self.rbQuiz.pack() # "quiz"

        self.rbBancAccount = Radiobutton(text="banc account", variable=self.var, value=11)
        self.rbBancAccount.pack() # "banc account"

        self.rbChangeWorkingDirectory = Radiobutton(text="change working directory",
                                                    variable=self.var, value=12)
        self.rbChangeWorkingDirectory.pack() #"change working directory"

        self.rbCFManager_Tests = Radiobutton(text="manager tests",
                                                    variable=self.var, value=13)
        self.rbCFManager_Tests.pack()  # "manager tests"

        self.rbExit = Radiobutton(text="exit", variable=self.var, value=14)
        self.rbExit.pack() #"exit"

        self.butDoIt = Button(text="do it", command=self.rbrScaner)
        self.butDoIt.pack() #"do it"

        self.lblMain = Label(self.masterRoot, width=50, bg='white', fg='black')
        self.lblMain.pack()

        #self.masterRoot.mainloop()


    # ==================================================================================
    def rbrScaner(self):

        if self.var.get() == 0:
            self.lblMain['text'] = "create folder"
            cf=CreateFolder.test()
            print(cf)

        elif self.var.get() == 1:
            self.lblMain['text'] = "delete folder"
            dfd=DeleteFolder.test()
            print(dfd)

        elif self.var.get() == 2:
            self.lblMain['text'] = "delete file"
            df=DeleteFile.test()
            print(df)

        elif self.var.get() == 3:
            self.lblMain['text'] = "copy folder"
            CopyFolder.test()

        elif self.var.get() == 4:
            self.lblMain['text'] = "copy file"
            CopyFile.test()

        elif self.var.get() == 5:
            self.lblMain['text'] = "view the contents of the working directory"
            vtcotwd=ViewTheContentsOfTheWorkingDirectory.test()
            print(vtcotwd)

        elif self.var.get() == 6:
            self.lblMain['text'] = "see only folders"
            sofolds = SeeOnlyFolders.test()
            print(sofolds)

        elif self.var.get() == 7:
            self.lblMain['text'] = "see only files"
            sofils = SeeOnlyFiles.test()
            print(sofils)

        elif self.var.get() == 8:
            self.lblMain['text'] = "see operation system information"
            sosi=SeeOperationSystemInformation.test()
            print(sosi)

        elif self.var.get() == 9:
            self.lblMain['text'] = "program creator"

            ProgramCreator.test()
            # для ProgramCreator отдельный выход
            self.quitProgramCreator()

        elif self.var.get() == 10:
            self.lblMain['text'] = "quiz"
            qt=Quiz.test(3)    # количество заходов в игре
            print(qt)

        elif self.var.get() == 11:
            self.lblMain['text'] = "banc account"
            BancAccount.test()

        elif self.var.get() == 12:
            self.lblMain['text'] = "change working directory"
            ChangeWorkingDirectory.test()

        elif self.var.get() == 13:
            self.lblMain['text'] = "manager tests"
            # CFManager_Tests.test('__main__')
            #runpy.run_module('C:\PythonDrom\Tests_2022\CFManager_tst\CFManager_Tests')
            #runpy.run_module('CFManager_Tests', run_name='__main__')
            runpy.run_module(mod_name='CFManager_Tests', init_globals=None, run_name='__main__')
            #CFManager_Tests.unittest.main()

        elif self.var.get() == 14:
            self.lblMain['text'] = "exit"
            # по команде exit производится
            # выход из цикла обработки событий
            self.masterRoot.quit()
            # а потом из masterRoot.rbrScaner
            # управление передаётся в main,
            # где выполняется exit(0)


    def quitProgramCreator(self):
        self.quit()

    def quit(self):
        sys.exit(0)
        main(0)


def main(key = 1):
    if key == 1:
        cfm = CFManager("rbrScaner")
        cfm.masterRoot.mainloop()
    elif key == 0:
        sys.exit(0)


if __name__ == '__main__':
    main(1)

# ========================================================================
