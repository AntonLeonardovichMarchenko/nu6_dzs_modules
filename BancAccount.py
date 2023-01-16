
"""
В приложении объявлено три класса:

BancAccount - банковский счёт. Объекты этого класса имеют два атрибута:
        идентификатор BancAccountID и сумма на счёте account. Реализованы методы
        изменения суммы (достаточно одного - plus) и метод printAccount для
        представления банковского счёта.

Banc - банк. Это класс со статическими методами
        CreateBancAccount(...): С открытием первого
        счёта создаётся файл для записи истории банковских операций bncDep.txt,
        добавление объекта BancAccount в список Banc.BancAccounts.
        в банке реализованы варианты поиска объектов BancAccount
        по ключу в словаре (BancAccountID: BancAccount)
        (для этого сделан словарь Banc.DictAccounts) и по номеру объекта в списке
        банковских счетов. Метод класса позволяет обновлять список счетов из
        файл записи истории банковских операций bncDep.txt.
        Изменения состояния счёта также фиксируются в файле bncDep.txt.

        getBancAccountByNum(...): извлечение счёта из списка счетов по его номеру
        в списке (словаре) счетов. Сначала получается список ключей из словаря
        Banc.DictAccounts, в этом списке находится соответствующий ключ
        и если возможно(!) по этому ключу из словаря счетов достаётся счёт.

        changeBancAccountByNum(...): изменение счёта, извлечённого по его номеру.
        Измененение состояния счёта фиксируется в файле для записи истории банковских
        операций bncDep.txt.

        getBancAccountByKey(...): извлечение счёта из списка счетов по его ключу
        в списке (словаре) счетов.

        changeBancAccountByKey(...): изменение счёта, извлечённого по его ключу.
        Измененение состояния счёта фиксируется в файле для записи истории банковских
        операций bncDep.txt.

        getBancAccountsFromFileManager(): чтение из файла истории банковских
        операций bncDep.txt.

        AppendBancAccount(...): в тестовом варианте(!!!) добавление нового(!!!)
        счёта в список (словарь) счетов сейчас добавление производится поcле
        чтения информации из файла счетов.

        closeBanc(): закрытие файла истории банковских операций bncDep.txt.

class FileManagerBanc: с помощью методов этого класса осуществляется работа
        с файлом истории банковских операций bncDep.txt.

        __init__(self, key): создаётся банковская директория DepotDirName с файлом
        DepotFileName depot\bncDep.txt

        fileManagerBancForRead(...): метод класса (classmethod) для работы с
        файлом истории банковских операций bncDep.txt
        - проверка на существование файла в директории depot\bncDep.txt
        - файл в директории Depot существует и может быть открыт на чтение

        fileBancAccountClose(...): закрытие файла истории банковских операций bncDep.txt.

Истории купленных товаров НЕТ

"""

import os
from pathlib import Path
import array

def test():
    print('this is BancAccount')
    doIt()

def doIt():

#========== Создаются (или читаются) 3 банковских счёта =================================


    if FileManagerBanc.filePathAndFileIsOK() == True:
            Banc.FMB = FileManagerBanc('r')
            print(f'OK! {FileManagerBanc.fbp} exist ')

            Banc.BancAccounts.clear()  # Очистить список! Сейчас чтение из файла счетов.

            try:
                for line in Banc.FMB.bf:

                    lineBancAccount = line.strip()
                    accElements = lineBancAccount.split(' ')

                    bnc = BancAccount(accElements[0], float(accElements[1]))
                    Banc.BancAccounts.append(bnc)
                    Banc.DictAccounts[bnc.BancAccountID] = bnc

                # Прочитали записи из файла истории счетов
            finally:
                # в тестовом варианте(!!!) добавление нового(!!!) счёта =================
                # в список (словарь) счетов поcле чтения информации из файла счетов.
                Banc.AppendBancAccount()
                # =======================================================================
                Banc.closeBanc()
                # закрыли файл счетов
    else:

        FileManagerBanc.fbp = ''

        Banc.CreateBancAccount(15.00)
        Banc.CreateBancAccount(250.00)
        Banc.CreateBancAccount(27.00)
#========================================================================================

    Banc.typeBancAccounts()

#========================================================================================

    print(f'~~~~~~~~~~Banc.changeBancAccountByNum~~~~~~~~~~~~~~~~~~~~')
    #  банковский счёт по номеру в списке счетов =========================
    Banc.changeBancAccountByNum(1, -10.0)
    Banc.typeBancAccounts()
    print(f'~~~~~~~~~~Banc.changeBancAccountByKey~~~~~~~~~~~~~~~~~~~~')
    #  банковский счёт по ключу в списке счетов ==========================
    Banc.changeBancAccountByKey(str(1), 11.0)
    Banc.typeBancAccounts()
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#========================================================================================
class BancAccount:

    def __init__(self, IDkey, initSum = 0.0):
        self.BancAccountID = str(IDkey)
        self.account = initSum

    def plus(self, summ):
        self.account = self.account + summ

    def minus(self, summ):
        self.account = self.account - summ

    def printAccount(self):
        print(f'{self.BancAccountID}...{self.account} ')

#========================================================================================
class FileManagerBanc:

    DepotDirName = 'Depot'
    DepotFileName = 'bncDep.txt'

    fbp = None  #  file banc path
    bf = None   #  banc file


    def __init__(self, key):
        # создаётся банковская директория DepotDirName с файлом DepotFileName ===========
        # 'depot\bncDep.txt

        CurrentWD = os.getcwd()
        BancPath = CurrentWD + '\\' + FileManagerBanc.DepotDirName

        if os.path.exists(BancPath) == False:
            print(f'~1~: {BancPath} is not exist')
            os.mkdir(BancPath)


        FileManagerBanc.fbp = BancPath + '\\' + FileManagerBanc.DepotFileName
        FileManagerBanc.bf = open(FileManagerBanc.fbp, key)

    # файл с информацией о счетах проверяется на существование. =========================

    @classmethod
    def fileManagerBancForRead(cls):

        print(f'this is fileManagerBancForRead')
        # проверка на существование файла в директории Depot
        if os.path.exists(FileManagerBanc.fbp) == False:
            # файла в директории Depot не существует. Поздняк метаться...
            print(f'<1>: {FileManagerBanc.fbp} is not exist')
            return False
        else:
            # файл в директории Depot существует и может быть открыт на чтение
            print(f'<2>: {FileManagerBanc.fbp} is exist')
            return True
    #====================================================================================

    @classmethod
    def filePathAndFileIsOK(cls):
        CurrentWD = os.getcwd()
        BancPath = CurrentWD + '\\' + FileManagerBanc.DepotDirName
        FileManagerBanc.fbp = BancPath + '\\' + FileManagerBanc.DepotFileName
        result0 = os.path.exists(BancPath) and os.path.exists(FileManagerBanc.fbp)
        if result0 is False:
            FileManagerBanc.fbp = ''
            return False

        f = Path(FileManagerBanc.fbp)
        size = os.path.getsize(f)
        if size > 0:
            return True
        else:
            FileManagerBanc.fbp = ''
            return False

    #====================================================================================

    def fileBancAccountClose(self):
        self.bf.close()
#========================================================================================

class Banc:

    FMB = None
    CurrentBancAccountID = 0
    BancAccounts = []      # Список банковских счетов
    DictAccounts = {}      # Словарь банковских счетов.
                           # Ключ - BancAccountID, значение - объект BancAccount

    @staticmethod
    def CreateBancAccount(Acc=10.00):

        # С первым счётом создаётся файл для записи
        # истории банковских операций 'bncDep.txt' если его не было ======
        if Banc.FMB is None:
            Banc.FMB = FileManagerBanc('w')
        else:
            try:
                # Ранее созданный файл открывается =======================
                Banc.FMB.bf = open(Banc.FMB.fbp, 'a')
            except Exception as ex:
                # что-то пошло не так... =================================
                print(f'{ex}')
                exit(0)

        # если файл всё-таки открылся... ==================
        bf = Banc.FMB.bf
        # начинактся работа с файлом истории банковских ===
        # операций 'bncDep.txt': создаётся счёт, который ==
        # добавляется в список Banc.BancAccounts ==========
        # =================================================

        Banc.CurrentBancAccountID = Banc.CurrentBancAccountID + 1

        # CurrentBancAccountID: примитивный механизм создания идентификатора
        # (ключа банковского счёта). Реализован на основе целых (int).
        bnc = BancAccount(Banc.CurrentBancAccountID, Acc)
        # при создании нового банковского счёта на него начисляются
        # премиальные 10 бонусов
        #
        # bnc.printAccount()

        # добавление объекта bnc в список Banc.BancAccounts
        Banc.BancAccounts.append(bnc)
        # в банке реализован поиск объекта BancAccount
        # по ключу в словаре (BancAccountID: BancAccount)
        # для этого сделан словарь Banc.DictAccounts.
        # добавление объекта bnc в словарь по ключу bnc.BancAccountID
        Banc.DictAccounts[bnc.BancAccountID] = bnc

        # # Список ключей в словаре
        # xKeys = Banc.DictAccounts.keys()
        # print(f'the list of keys in Banc.DictAccounts >>>>> {xKeys} <<<<<')

        # ====== строка с инфой о счёте записывается в bncDep.txt =======================
        stringBancInfo = bnc.BancAccountID + ' ' + str(bnc.account) + '\n'
        try:
            bf.write(stringBancInfo)
        finally:
            Banc.closeBanc()
            # после действий с FileManagerBanc (запись строки счёта)
            # файл bncDep.txt (история банковских операций) закрывается
        # ===============================================================================
        ## это проверка файла bf (истории банковских операций)
        # Banc.getBancAccountsFromFileManager()
        # ===============================================================================
        #  проверка списка счетов в Banc.BancAccounts
        # Здесь важно правильно спрашивать о количестве открытых в банке счетов и
        #             правильно читать записанную в счетах информацию.
        i = 0
        for bnc in Banc.BancAccounts:
            print(f'{i}....{bnc.BancAccountID}....{bnc.account}')
            i += 1
        print(f'------------------------------------------------')
        # ===============================================================================


    @staticmethod
    def AppendBancAccount(Acc=10.00):
        # в тестовом варианте(!!!) добавление нового(!!!) счёта
        # в список (словарь) счетов поcле чтения информации из файла счетов.
        # Список ключей в словаре. Ключ сделан на основе целого числа.
        # Сделать его на основе float не смог...
        xKeys = list(Banc.DictAccounts.keys())
        print(f'the list of keys in Banc.DictAccounts ~~~~~ {xKeys} ~~~~~')

        xN = len(xKeys)
        xN -= 1

        lastKey = int(xKeys[xN])
        newKey = lastKey + 1
        print(f'{newKey}')
        bnc = BancAccount(newKey, Acc)  # при создании нового
        #  банковского счёта на на него начисляются премиальные 10 бонусов

        # и добавили ещё один счёт ===============================
        # добавление объекта bnc в список Banc.BancAccounts
        Banc.BancAccounts.append(bnc)
        # в банке реализован поиск объекта BancAccount
        # по ключу в словаре (BancAccountID: BancAccount)
        # для этого сделан словарь Banc.DictAccounts.
        # добавление объекта bnc в словарь по ключу bnc.BancAccountID
        Banc.DictAccounts[bnc.BancAccountID] = bnc
        # =========================================================

    @staticmethod
    def getBancAccountByNum(num):
        # получить список ключей
        listOfKeys = list(Banc.DictAccounts.keys())
        try:
            # если возможно(!) из него достать num-й ключ
            accKey = listOfKeys[num]
        except IndexError as err:
            print(f'Key {num}: {err}')
            return None
        # и по этому ключу из словаря счетов достать счёт
        bnc = Banc.DictAccounts[accKey]

        print(f'{num} > {accKey}: {bnc.BancAccountID}....{bnc.account}')
        return bnc

    @staticmethod
    def changeBancAccountByNum(num, summ):
        bnc = Banc.getBancAccountByNum(num)
        if bnc != None:
            if summ != 0.0:
                bnc.plus(summ)

                newBNC = BancAccount(bnc.BancAccountID, bnc.account)
                Banc.DictAccounts[bnc.BancAccountID] = newBNC
                Banc.BancAccounts[num] = newBNC

                # проверка на корректное изменение счёта в словаре
                print(f'****************************************')
                values = Banc.DictAccounts.values()
                for v in values:
                    v.printAccount()
                print(f'****************************************')

                # ============== строка с инфой о счёте =========================================

            try:
                # открывается файл для записи истории банковских операций 'bncDep.txt'
                Banc.FMB.bf = open(Banc.FMB.fbp, 'w').close()  # удаление старых записей
                Banc.FMB.bf = open(Banc.FMB.fbp, 'a')  # открытие пустого словаря
                # Ранее созданный файл открывается ======================================
                # список значений из словаря
                for value in Banc.BancAccounts:
                    stringBancInfo = value.BancAccountID + ' ' + str(value.account) + '\n'
                    Banc.FMB.bf.write(stringBancInfo)  # запись стоки в 'bncDep.txt'
            finally:
                Banc.FMB.fileBancAccountClose()  # после действий с FileManagerBanc
            # (запись ВСЕХ строк счёта) файл закрывается
            # ===============================================================================

    @staticmethod
    def getBancAccountByKey(accKey):

        # здесь проще. Ключ задан и по этому ключу (если это возможно)
        # из словаря достать счёт =======================================================
        try:
            bnc = Banc.DictAccounts[accKey]
        except Exception:
            print(f'key error: {accKey}')
            return None

        print(f'{accKey}: {bnc.BancAccountID}....{bnc.account}')
        return bnc
        #================================================================================

    @staticmethod
    def changeBancAccountByKey(accKey, summ):
        bnc = Banc.getBancAccountByKey(accKey)
        if bnc != None:
            if summ != 0.0:
                bnc.account = bnc.account + summ
                newBNC = BancAccount(accKey, bnc.account)
                Banc.DictAccounts[accKey] = newBNC

                # проверка на корректное изменение счёта в словаре
                print(f'****************************************')
                values = Banc.DictAccounts.values()
                for v in values:
                    v.printAccount()
                print(f'****************************************')

            # ============== строка с инфой о счёте =========================================

            try:
                # открывается файл для записи истории банковских операций 'bncDep.txt'
                Banc.FMB.bf = open(Banc.FMB.fbp, 'w').close()  # удаление старых записей
                Banc.FMB.bf = open(Banc.FMB.fbp, 'a')    # открытие пустого словаря
                # Ранее созданный файл открывается ======================================
                values = Banc.DictAccounts.values()    # список значений из словаря
                for v in values:
                    stringBancInfo = v.BancAccountID + ' ' + str(v.account) + '\n'
                    Banc.FMB.bf.write(stringBancInfo)    # запись стоки в 'bncDep.txt'
            finally:
                Banc.FMB.fileBancAccountClose()  # после действий с FileManagerBanc
                                                 # (запись ВСЕХ строк счёта) файл закрывается
        # ===============================================================================

    @staticmethod
    def typeBancAccounts():
        i = 0
        for bnc in Banc.BancAccounts:
            print(f'******{i}***********')
            bnc.printAccount()
            print(f'\n')
            i+=1

    @staticmethod
    def getBancAccountsFromFileManager():
        if Banc.FMB.fileManagerBancForRead() == True:
            # print('_____ getBancAccountsFromFileManager success ! _____')
            Banc.BancAccounts.clear()  # Очистить список! Сейчас чтение из файла счетов.
            FileManagerBanc.bf = open(FileManagerBanc.fbp, 'r')

            try:
                for line in FileManagerBanc.bf:

                    lineBancAccount = line.strip()
                    accElements = lineBancAccount.split(' ')

                    ba = BancAccount(accElements[0], float(accElements[1]))
                    Banc.BancAccounts.append(ba)

                # Прочитали записи из файла счетов
            finally:
                Banc.closeBanc()
                # закрыли файл счетов


        Banc.typeBancAccounts()


    @ staticmethod
    def closeBanc():
        Banc.FMB.fileBancAccountClose()

#========================================================================================

