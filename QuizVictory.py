'''
Модуль victory.py.
Написать или улучшить программу Викторина из предыдущего дз
(Для тренировки не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') -
предлается для тренировки пока(!!!) использовать строку...
Программа выбирает 5 случайных людей из 10,
это можно реализовать с помощью модуля random и функции sample

Пример использования sample:
# ===================================================================
import random
numbers = [1, 2, 3, 4, 5]
# 2 - количество случайных элементов
result = random.sample(numbers, 2)
print(result) # [5, 1]
# ===================================================================
После того как выбраны 5 случайных людей,  пользователю предлагается
ввести их дату рождения.
дата вводится в формате 'dd.mm.yyyy'
Например 03.01.2009, если пользователь ответил неверно,
то выводится правильный ответ, но уже в следующем виде (формате):
третье января 2009 года
(склонением можно пренебречь)...
В конце считается количество правильных и неправильных ответов
и предлагаем начать игру снова
'''

#import datetime

import random
from random import randrange

class TheBornExpert:

    QuizNum = 0

    resOfQuizRound = [False]*10

    Persons = [[], [], []]
    PersonsMonitor = []

    keysDays = []
    Days = {}
    keysMonths = []
    Months = {}

    # BornDay = None
    # BornMonth = None
    # BornYear = None

    @staticmethod
    def InitListOfPersonsDepo():

        i = 0
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Stalin')
        TheBornExpert.Persons[2].append('21.12.1879')

        i += 1
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Marx')
        TheBornExpert.Persons[2].append('5.5.1818')

        i += 1
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Engels')
        TheBornExpert.Persons[2].append('28.11.1820')

        i += 1
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Mussolini')
        TheBornExpert.Persons[2].append('29.7.1883')

        i += 1
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Hitler')
        TheBornExpert.Persons[2].append('20.4.1889')

        i += 1
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Bizet')
        TheBornExpert.Persons[2].append('25.10.1838')

        i += 1
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Zedong')
        TheBornExpert.Persons[2].append('26.12.1893')

        i += 1
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Castro')
        TheBornExpert.Persons[2].append('13.8.1926')

        i += 1
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Gaddafi')
        TheBornExpert.Persons[2].append('7.6.1942')

        i += 1
        TheBornExpert.Persons[0].append(i)
        TheBornExpert.Persons[1].append('Mandela')
        TheBornExpert.Persons[2].append('18.7.1918')
    # ===================================================================================
    @staticmethod
    def fullDateFormer():
        # ===================================================================================
        TheBornExpert.Days = { 1:'первое',  2:'второе',  3:'третье',  4:'четвёртое',
                               5:'пятое',  6:'шестое',  7:'седьмое',  8:'восьмое',
                               9:'девятое',  10:'десятое', 11:'одиннадцатое', 12:'двенадцатое',
                               13:'тринадцатое', 14:'четырнадцатое', 15:'пятнадцатое',
                               16:'шестнадцатое', 17:'семнадцатое', 18:'восемнадцатое',
                               19:'девятнадцатое', 20:'двадцатое', 21:'двадцать первое',
                               22:'двадцать второе', 23:'двадцать третье',
                               24:'двадцать четвёртое', 25:'двадцать пятое',
                               26:'двадцать шестое', 27:'двадцать седьмое',
                               28:'двадцать восьмое', 29:'двадцать девятое',
                               30:'тридцатое', 31:'тридцать первое' }

        TheBornExpert.keysDays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                                  16,17,18,19,20,21,22,23,24,25,26,26,28,29,30,31]


    # ===================================================================================
        TheBornExpert.Months={ 1:'января', 2:'февраля', 3:'марта', 4:'апреля',
                               5:'мая', 6:'июня', 7:'июля', 8:'августа',
                                9:'сентября', 10:'октября', 11:'ноября', 12:'декабря'}

        TheBornExpert.keysMonths = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]

    # ===================================================================================

    @staticmethod
    def dayTester(bornDay):
        if int(bornDay) not in TheBornExpert.keysDays:
            raise ('The day exseption')

    @staticmethod
    def monthTester(bornMonth):
        if int(bornMonth) not in TheBornExpert.keysMonths:
            raise ('The month exseption')

    @staticmethod
    def yearTester(bornYear):
        # date = Persons[2][pIndex]
        # year = date[-4: : ]

        if len(bornYear) != 4 or bornYear.isdigit() == False:
            raise ('The year exseption')

    @staticmethod
    def DateTimeTest(quizNum):
        while True:
            TheBornExpert(quizNum)
            theResult = input('Continue the game? Yes/No > ')
            if theResult == 'No':
                break


    def __init__(self, quizNum):
        self.Persons = [[],[],[]]
    # ===================================================================================
        if len(TheBornExpert.Persons[0]) == 0:
            TheBornExpert.InitListOfPersonsDepo()
            TheBornExpert.fullDateFormer()
            TheBornExpert.QuizNum = quizNum
    # ===================================================================================
        self.Persons[1].clear()
        for i in range(5):
            persIndex = randrange(0, len(TheBornExpert.Persons[0]))
            self.Persons[0].append(i)
            self.Persons[1].append(TheBornExpert.Persons[1][persIndex])
            self.Persons[2].append(TheBornExpert.Persons[2][persIndex])

        for i in range(TheBornExpert.QuizNum):
            TheBornExpert.resOfQuizRound[i] = False
        else:
            self.quiz()
    # ===================================================================================


    def quiz(self):
    # ===================================================================================

        for i in range(len(self.Persons[0])):
            print(f'{self.Persons[1][i]} ... {self.Persons[2][i]}')

        TheBornExpert.PersonsMonitor = []
    # ===================================================================================

        nTrue = 0
        print(f'+------------------------------------------+')
        for i in range(TheBornExpert.QuizNum):
        # значение TheBornExpert.QuizNum берётся из main и здесь i это номер игры
            persIndex = randrange(0, len(self.Persons[0]))
            # случайный персонаж из списка. persIndex - это его индекс
            print(f'{i}:{self.Persons[1][persIndex]}')
            TheBornExpert.PersonsMonitor.append(persIndex)
            # сама игра. Точка входа и подсчёт успешных результатов ===========
            if self.bornTester(persIndex, i) == True:
                nTrue += 1
            # =================================================================

        # отыграли TheBornExpert.QuizNum игр с результатом nTrue ========================
        # вывод результатов TheBornExpert.QuizNum игр ===================================

        print(f'+------------------------------------------+')
        print(f'<< the result is {(nTrue*100)/TheBornExpert.QuizNum} >>')
        print(f'+------------------------------------------+')

        for i in range(0, TheBornExpert.QuizNum):
            n = TheBornExpert.PersonsMonitor[i]
            print(f'{i} > {self.Persons[1][n]} is {TheBornExpert.resOfQuizRound[i]}')
        # персональные результаты =======================================================
    # ===================================================================================

    def bornTester(self, persIndex, i):

        while True:
            try:
                print(f'+------------------------------------------+')
                print(f'|  what is the BornDay of {self.Persons[1][persIndex]} (d(d).m(m).yyy): ')
                print(f'| ', end=" ")
                self.bornDay = input('day > ')
                TheBornExpert.dayTester(self.bornDay)
                print(f'| ', end=" ")
                self.bornMonth = input('month > ')
                TheBornExpert.monthTester(self.bornMonth)
                print(f'| ', end=" ")
                self.bornYear = input('year > ')
                TheBornExpert.yearTester(self.bornYear)
                print(f'+------------------------------------------+')

                bornString = str(self.bornDay)+'.'+str(self.bornMonth)+'.'+str(self.bornYear)
                # bornString - это строка формата d(d).m(m).yyy

                break

            except Exception as ex:
                print(f'|   {ex} ')
                print(f'+------------------------------------------+')

        print(f'the Born Day of {self.Persons[1][persIndex]} is {bornString}')
        theResult = self.bornComparer(bornString, persIndex, i)
        return (theResult)

    def bornComparer(self, bornString, persIndex, i):
    #                      bornString - строка формата d(d).m(m).yyyy
    #                                  persIndex - индекс персонажа
    #                                             i - номер игры

        persBornString = self.dateBornFormator(str(self.Persons[2][persIndex]))

        if bornString == str(self.Persons[2][persIndex]):

            print(f'you are RIGHT!', end=" ")
            print(f' {self.Persons[1][persIndex]} was born {persBornString}')
            TheBornExpert.resOfQuizRound[i] = True   # результат текущей игры
            return True
        else:
            print(f'you are WRONG!', end=" ")
            print(f' {self.Persons[1][persIndex]} was born {persBornString}')
            return False

    # ===== в строчный формат =======================================
    def dateBornFormator(self, persBornString):

        ddd = persBornString.split('.')
        dayIndex = int(ddd[0])
        dayStr = TheBornExpert.Days[dayIndex]
        monthIndex = int(ddd[1])
        monthStr = TheBornExpert.Months[monthIndex]
        yearStr = ddd[2]
        return (dayStr+' '+monthStr+' '+yearStr)


