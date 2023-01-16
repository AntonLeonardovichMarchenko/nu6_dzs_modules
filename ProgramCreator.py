"""
НЕ НАШЁЛ ИНФОРМАЦИИ ОБ АВТОРЕ ПРОГРАММЫ. В интернете набрёл на интересную "заготовку".
В предлагаемом варианте проги интерфейс пользователя МОЙ. Реализация методов
частично (!) моя. Сами алгоритмы взяты из прототипа (куда уж нам...).
В любом случае, было интересно. Спасибо авторам.


Программа на PYTHON для определения авторства текста по частоте появления новых слов
в том числе, текстов программ на Python
*
Короткая история метода

В под названием “Авторство писателей можно узнать по специальной формуле” сообщалось,
что в научном издании «New Journal of Physics», группа шведских физиков из университета
Умео под руководством Себастьяна Бернгардсона описала новый метод,
который позволяет на основе статистических данных определить автора текста.
Исследователи проверяли, как в текстах трех писателей —
Томаса Харди, Генри Мелвилла и Дэвида Лоуренса — реализуется так называемый закон Ципфа.
Исследователи обнаружили, что частота появления новых слов по мере роста объема текста
меняется у разных авторов по-разному, причем эта закономерность не зависит от
конкретного текста, а только от автора.

Это сообщение было опубликовано 11.12.2009, а, более двадцати лет тому назад,
Джон Чарльз Бейкер ввел единицу для измерения способности автора использовать
новые слова (здесь понятие «новые» трактуется как ранее не используемые в данном тексте).
Джон Чарльз Бейкер доказал, что указанная единица является индивидуальной характеристикой
  автора.

В периодических изданиях и в сети отсутствует информация о реализации закона Зипфа
для определения авторства. Поэтому эта работа является первым научным исследованием
в указанной области.

Спасибо автору за интересную работу!

"""

import sys

import tkinter as T
from tkinter import *
from tkinter import END
from tkinter import filedialog as fd

from matplotlib import pyplot as plt
import matplotlib as mpl

import nltk
import numpy as np
from nltk import *
from nltk.corpus import brown
from nltk.tokenize import word_tokenize

"""
Python-библиотека nltk

nltk (Natural Language Toolkit) – платформа для создания NLP-программ на Python. 
У нее интерфейсы для многих языковых корпусов, библиотеки для обработки текстов
для классификации, токенизации, стемминга, разметки, фильтрации и семантических рассуждений.

В лингвистике кóрпус (в данном значении множественное число — кóрпусы, не корпусá(!!!)) 
— подобранная и обработанная по определённым правилам совокупность текстов, используемых
в качестве базы для исследования языка. Они используются для статистического анализа
и проверки статистических гипотез, подтверждения лингвистических правил в данном языке. 
Корпус текстов является предметом исследования корпусной лингвистики. 

Корпус — основное понятие и база данных корпусной лингвистики. 
Анализ и обработка разных типов корпусов являются предметом большинства работ 
в области компьютерной лингвистики (например, извлечение ключевых слов), 
распознавания речи и машинного перевода, в которых корпусы часто применяются
при создании скрытых марковских моделей для маркирования частей речи и других задач. 
Корпусы и частотные словари могут быть полезны в обучении иностранным языкам (ну да...).

Основные свойства корпуса (его главные свойства):
= электронный — в современном понимании корпус должен быть в электронном виде;
= репрезентативный — должен хорошо «представлять» объект, который моделирует
  размеченный — главное отличие корпуса от коллекции текстов;
= прагматически ориентированный —  создаётся под определённую задачу;

Корпусы можно классифицировать по различным признакам: 
цель создания корпуса, тип языковых данных, «литературность», 
жанр, динамичность, тип разметки, объём текстов и так далее. 
По критерию параллельности, например, корпусы можно разделить на 
одноязычные, двуязычные и многоязычные. 
Многоязычные и двуязычные делятся на два типа:
= параллельные — множество текстов и их переводов на один или несколько языков.
= сопоставимые (псевдопараллельные) — оригинальные тексты на двух или нескольких языках.

Разметка корпусов
Заключается в приписывании текстам и их компонентам специальных тегов: 
лингвистических и внешних (экстралингвистических). 
Выделяют следующие лингвистические типы разметки: 
морфологическая, семантическая, синтаксическая, анафорическая, 
просодическая, дискурсная и т. д.
К некоторым корпусам применяются дальнейшие структурные уровни анализа. 
В частности, некоторые небольшие корпусы могут быть полностью синтаксически размечены. 
Такие корпусы обычно называют глубоко аннотированными или синтаксическими, 
а сама синтаксическая структура при этом является деревом зависимостей.

Ручная разметка (аннотирование) текстов
(!!!) дорогостоящая и трудоемкая задача (!!!). 
На данный момент в открытом доступе представлены различные программные средства 
для разметки корпусов[3]. Условно их можно разделить 
на обособленные (stand-alone) и веб-ориентированные (web-based). 
При этом акцент разработчиков сместился в сторону веб-приложений. 
Данные системы обладают рядом преимуществ:

= возможность одновременной разметки одного документа несколькими людьми
= не требуют установки дополнительных программных средств, кроме браузера
= гибкое разграничение прав доступа
= отображение текущего прогресса процесса разметки
= возможность модификации размечаемого корпуса
(бла-бла-бла)

Можно создавать «веб-корпусы», то есть корпусы, 
полученные путём обработки интернет-источников:

Веб-корпус представляет собой особый вид лингвистического корпуса, 
который создан путем постепенной загрузки текстов из интернета 
при помощи автоматизированных процедур, которые на лету определяют язык и 
кодировку отдельных веб страниц, удаляют шаблоны, элементы навигации, ссылки и рекламу
(т. н. boilerplate), осуществляют трансформацию на текст, фильтрацию, нормализацию
и дедупликацию полученных документов, 
которые затем можно обработать традиционными инструментами корпусной лингвистики 
(токенизация, мирфосинтаксическая и синтаксическая аннотация) и 
внедрить в поисковую корпусную систему. При этом создание веб-корпуса намного дешевле, 
его размер может быть даже на порядок больше традиционных корпусов.

Компью́терная лингви́стика — научное направление в области математического и 
компьютерного моделирования интеллектуальных процессов у человека и животных (говорящих) 
при создании систем искусственного интеллекта. (типа, понятно)

Ключевое слово — слово в тексте, способное в совокупности с другими ключевыми словами
представлять текст. используется главным образом для поиска.

Распознавание речи — автоматический процесс преобразования речевого сигнала
в цифровую информацию. Обратной задачей является синтез речи.

Скрытая марковская модель (СММ) — статистическая модель, имитирующая работу процесса, 
похожего на марковский процесс с неизвестными параметрами. Её задачей ставится 
разгадывание неизвестных параметров на основе наблюдаемых.

Часто́тный слова́рь — набор слов данного языка вместе с информацией об их частотности. 
Словарь может быть отсортирован 
= по частотности, 
= по алфавиту, 
= по группам слов,
= по типичности, и т. д. 

1. Токенизация по предложениям
Токенизация (иногда – сегментация) по предложениям – это процесс разделения письменного языка на предложения-компоненты. 
Идея выглядит довольно простой. В английском и некоторых других языках мы можем вычленять предложение каждый раз, 
когда находим определенный знак пунктуации – точку.

Но даже в английском эта задача нетривиальна, так как точка используется и в сокращениях. 
Таблица сокращений может сильно помочь во время обработки текста, чтобы избежать неверной расстановки границ предложений. 
В большинстве случаев для этого используются библиотеки, так что можете особо не переживать о деталях реализации (!!!).

Пример:

Текст про настольную игру нарды:

Backgammon is one of the oldest known board games. 
Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East. 
It is a two player game where each player has fifteen checkers which move between twenty-four 
points according to the roll of two dice.

Чтобы сделать токенизацию предложений с помощью NLTK, можно воспользоваться методом nltk.sent_tokenize...
На выходе получается 3 отдельных предложения:

Backgammon is one of the oldest known board games.
Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East.
It is a two player game where each player has fifteen checkers which move between twenty-four 
points according to the roll of two dice.

2. Токенизация по словам

Токенизация (иногда – сегментация) по словам – это процесс разделения предложений на слова-компоненты. 
В английском и многих других языках, использующих ту или иную версию латинского алфавита, 
пробел – это неплохой разделитель слов.
Тем не менее, могут возникнуть проблемы, если будет использован только пробел – 
в английском составные существительные пишутся по-разному и иногда через пробел. И тут вновь 
помогают библиотеки.

Пример:

Взять предложения из предыдущего примера и применить к ним метод nltk.word_tokenize.
Вывод:

['Backgammon', 'is', 'one', 'of', 'the', 'oldest', 'known', 'board', 'games', '.']

['Its', 'history', 'can', 'be', 'traced', 'back', 'nearly', '5,000', 'years', 'to', 'archeological', 
'discoveries', 'in', 'the', 'Middle', 'East', '.']

['It', 'is', 'a', 'two', 'player', 'game', 'where', 'each', 'player', 'has', 'fifteen', 'checkers', 
'which', 'move', 'between', 'twenty-four', 'points', 'according', 'to', 'the', 'roll', 'of', 'two', 'dice', '.']

3. Лемматизация и стемминг текста

Обычно тексты содержат разные грамматические формы одного и того же слова, а также могут встречаться однокоренные слова. 
Лемматизация и стемминг преследуют цель привести все встречающиеся словоформы к одной, нормальной словарной форме.
Примеры:

Приведение разных словоформ к одной:
dog, dogs, dog’s, dogs’ => dog

То же самое, но уже применительно к целому предложению:
the boy’s dogs are different sizes => the boy dog be differ size

Лемматизация и стемминг – это частные случаи нормализации и они различаются.
Стемминг – это грубый эвристический процесс, который отрезает «лишнее» от корня слов, 
часто это приводит к потере словообразовательных суффиксов.

Лемматизация – это более тонкий процесс, который использует словарь и морфологический анализ, 
чтобы в итоге привести слово к его канонической форме – лемме.

Отличие в том, что стеммер (конкретная реализация алгоритма стемминга) действует без знания контекста и,
соответственно, не понимает разницу между словами, которые имеют разный смысл в зависимости от части речи. 
Однако у стеммеров есть и свои преимущества: их проще внедрить и они работают быстрее. 
Плюс, более низкая «аккуратность» может не иметь значения в некоторых случаях.

"""

# ==================== список кодировок при прочтении файлов =================================

encodings = ('utf-16', 'utf-8', 'cp1251', 'unicode')

# =================== Статические переменные для обозначения текстовых полей ==================

global root
root = None

global txt0
global txt1
global txt2
global txt3
global txt4
global txt5

global iMR

global fig, ax

global y1Data3, y1Data2, y1Data1, \
    xData1, xData2, xData3, \
    yData1, yData2, yData3

# =============== задание жанров для определения ==============================================

genres = ['news', 'editorial', 'reviews', 'religion', 'hobbies', 'lore',
          'belles_lettres', 'government', 'learned', 'fiction', 'mystery',
          'science_fiction', 'adventure', 'romance', 'humor']

# =============================================================================================

stop_words = nltk.corpus.stopwords.words('english')
mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Comic Sans MS, Arial'
from nltk.stem import SnowballStemmer

stop_symbols = '.,!?:;"-\n\r()'


# ============================================================================================

def test():
    global root
    # это вызов применяется при повторном запуске
    # модуля: закрывается старое окно ===========
    if root is not None:
        close_win()
    # ===========================================

    start_win()
    return 0


# ============================================================================================

def comor_text():
    global fig, ax, \
        y1Data3, y1Data2, y1Data1, \
        xData1, xData2, xData3, \
        yData1, yData2, yData3

    # функция стемминга NLTK - быстрее чем словарная лемитизация
    stemmer = SnowballStemmer('english')

    # контроль корректности данных
    if len(txt0.get(1.0, END)) != 1 and len(txt1.get(1.0, END)) != 1 and len(txt2.get(1.0, END)) != 1:

        mrus = [txt0.get(1.0, END), txt1.get(1.0, END), txt2.get(1.0, END)]
        mr = 3  # переменная для раздельного анализа графиков

    elif len(txt0.get(1.0, END)) != 1 and len(txt1.get(1.0, END)) != 1 and len(txt2.get(1.0, END)) == 1:
        mrus = [txt0.get(1.0, END), txt1.get(1.0, END)]
        mr = 2

    elif len(txt0.get(1.0, END)) != 1 and len(txt1.get(1.0, END)) == 1 and len(txt2.get(1.0, END)) == 1:
        mrus = [txt0.get(1.0, END)]
        mr = 1

    else:
        txt3.insert(END, "There are no all texts")
        return

    # стемминг, отбор стоп слов и создание частотных словарей
    for text in mrus:

        v = (
            [stemmer.stem(x) for x in [y.strip(stop_symbols) for y in text.lower().split()] if
             x and (x not in stop_words)])
        # частотный словарь. частота употребления слова - ранг слова
        my_dictionary = dict([])
        z = []

        for w in v:

            if w in my_dictionary:
                my_dictionary[w] += 1
            else:
                my_dictionary[w] = 1

        max_count = int(txt5.get(1.0, END))
        min_count = int(txt4.get(1.0, END))

        if len(my_dictionary) < max_count:
            txt3.insert(END, "It is not enough of words for the analysis ")
            return

        # частотный словарь частота употребления слова - количество слов
        my_dictionary_z = dict([])
        for key, val in my_dictionary.items():
            if val in my_dictionary_z:
                my_dictionary_z[val] += 1
            else:
                my_dictionary_z[val] = 1
            z.append(val)
        z.sort(reverse=True)

        # получение исходных данных для построения
        # графиков частотного распределения

        e = z[min_count:max_count]
        # ee = [my_dictionary_z[val] for val in z][min_count:max_count]  # ???
        ee = np.arange(len(my_dictionary))[min_count:max_count]  # ???

        xData1 = ee
        xData2 = ee
        xData3 = ee

        yData1 = e
        yData2 = e
        yData3 = e

        if text == mrus[0]:  # расчёт гиперболической аппроксимации -a,b для первого документа
            #  + % новых слов

            zz = round((float(len(my_dictionary)) * 100) / (float(len(v))), 0)
            tt = ('In total of words (Text-1) --%i. New words --%i. Percen new words-- %i' % (
                len(v), len(my_dictionary), int(zz)))
            # xData1 = ee
            # yData1 = e
            z = [1 / w for w in ee]
            z1 = [(1 / w) ** 2 for w in ee]
            t = [round(e[i] / ee[i], 4) for i in range(0, len(ee))]
            a = round((sum(e) * sum(z1) - sum(z) * sum(t)) / (len(ee) * sum(z1) - sum(z) ** 2), 3)
            b = round((len(ee) * sum(t) - sum(z) * sum(e)) / (len(ee) * sum(z1) - sum(z) ** 2), 3)
            y1 = [round(a + b / w, 4) for w in ee]

            y1Data1 = y1

            s = [round((y1[i] - e[i]) ** 2, 4) for i in range(0, len(ee))]
            sko = round(round((sum(s) / (len(ee) - 1)) ** 0.5, 4) / (sum(y1) / len(ee)), 4)
            tg = 'Factor --a  ' + str(a) + '  Factor--b  ' + str(b) + ' Mistake of approximation--  ' + str(
                sko) + "%" + "\n" + tt
            txt3.delete(1.0, END)
            txt3.insert(END, tg)
            txt3.insert(END, '\n')
            # y1Data2 = y1   # ??????????????????????????????????
            # y1Data3 = y1   # ??????????????????????????????????

        elif text == mrus[1]:  # расчёт аппроксимации -a,b для втого документа
            # + % новых слов

            zz = round((float(len(my_dictionary)) * 100) / (float(len(v))), 0)
            tt = ('In total of words (Text-2) --%i. New words --%i. Percent new words-- %i' % (
                len(v), len(my_dictionary), int(zz)))
            # xData2 = ee
            # yData2 = e
            z = [1 / w for w in ee]
            z1 = [(1 / w) ** 2 for w in ee]
            t = [round(e[i] / ee[i], 4) for i in range(0, len(ee))]
            a = round((sum(e) * sum(z1) - sum(z) * sum(t)) / (len(ee) * sum(z1) - sum(z) ** 2), 3)
            b = round((len(ee) * sum(t) - sum(z) * sum(e)) / (len(ee) * sum(z1) - sum(z) ** 2), 3)
            y1 = [round(a + b / w, 4) for w in ee]

            y1Data2 = y1

            s = [round((y1[i] - e[i]) ** 2, 4) for i in range(0, len(ee))]
            sko = round(round((sum(s) / (len(ee) - 1)) ** 0.5, 4) / (sum(y1) / len(ee)), 4)
            tg = 'Factor --a  ' + str(a) + '  Factor--b  ' + str(b) + ' Mistake of approximation--  ' + str(
                sko) + "%" + "\n" + tt
            txt3.insert(END, tg)
            txt3.insert(END, '\n')

            # y1Data1 = y1    # ??????????????????????????????????

            # y1Data3 = y1    # ??????????????????????????????????

        elif text == mrus[2]:  # расчёт аппроксимации -a,b для третьего документа
            #  + % новых слов

            zz = round((float(len(my_dictionary)) * 100) / (float(len(v))), 0)
            tt = ('In total of words (Text-3) --%i. New words --%i. Percent new words-- %i' % (
                len(v), len(my_dictionary), int(zz)))
            # xData3 = ee
            # yData3 = e
            z = [1 / w for w in ee]
            z1 = [(1 / w) ** 2 for w in ee]
            t = [round(e[i] / ee[i], 4) for i in range(0, len(ee))]
            a = round((sum(e) * sum(z1) - sum(z) * sum(t)) / (len(ee) * sum(z1) - sum(z) ** 2), 3)
            b = round((len(ee) * sum(t) - sum(z) * sum(e)) / (len(ee) * sum(z1) - sum(z) ** 2), 3)
            y1 = [round(a + b / w, 4) for w in ee]

            y1Data3 = y1

            s = [round((y1[i] - e[i]) ** 2, 4) for i in range(0, len(ee))]
            sko = round(round((sum(s) / (len(ee) - 1)) ** 0.5, 4) / (sum(y1) / len(ee)), 4)
            tg = 'Factor --a  ' + str(a) + '  Factor--b  ' + str(b) + ' Mistake of approximation--  ' + \
                 str(sko) + "%" + "\n" + tt
            txt3.insert(END, tg)
            txt3.insert(END, '\n')

            # y1Data1 = y1  # ??????????????????????????????????
            # y1Data2 = y1  # ??????????????????????????????????

    if mr == 3:  # построение графиков для первого и третьего документа +
        # среднее расстояние между их аппроксимацией

        r12 = round(sum([abs(yData1[i] - yData2[i]) for i in range(0, len(xData1))]) / len(xData1), 3)
        txt3.insert(END, "Average distances between art products of the author K--" + str(r12))
        txt3.insert(END, '\n')
        r13 = round(sum([abs(yData1[i] - yData3[i]) for i in range(0, len(xData1))]) / len(xData1), 3)
        txt3.insert(END, "Average distance between art products of the authors K and M--" + str(r13))
        txt3.insert(END, '\n')

        fig.clear(True)
        ax.clear()

        plt.title('Distribution of frequencies of use of words in the text', size=14)
        plt.xlabel('Serial number of new words', size=14)
        plt.ylabel('Frequency of the use of new words', size=14)
        plt.plot(xData1, yData1, color='r', linestyle=' ', marker='o', label='Test art product of the author -К')
        plt.plot(xData1, y1Data1, color='r', linewidth=2, label='Approximation of hyperbola y=(b/x)+a')
        plt.plot(xData2, yData2, color='g', linestyle=' ', marker='o', label='Comparable art product of the author -К')
        plt.plot(xData2, y1Data2, color='g', linewidth=2, label='Approximation of hyperbola y=(b/x)+a')
        plt.plot(xData3, yData3, color='b', linestyle=' ', marker='o', label='Art product of the author -М')
        plt.plot(xData3, y1Data3, color='b', linewidth=2, label='Approximation of hyperbola y=(b/x)+a')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()

    elif mr == 2:  # построение графиков для первого и второго документа +
        # среднее расстояние между их аппроксимацией

        r12 = round(sum([abs(yData1[i] - yData2[i]) for i in range(0, len(xData1))]) / len(xData1), 3)
        txt3.insert(END, "Average distances between art products of the author K--" + str(r12))
        txt3.insert(END, '\n')

        fig.clear(True)
        ax.clear()

        plt.title('Distribution of frequencies of use of words in the text', size=14)
        plt.xlabel('Serial number of new words', size=14)
        plt.ylabel('Frequency of the use of new words', size=14)
        plt.plot(xData1, yData1, color='r', linestyle=' ', marker='o', label='Test art product of the author -К')
        plt.plot(xData1, y1Data1, color='r', linewidth=2, label='Approximation of hyperbola y=(a/x)+b')
        plt.plot(xData2, yData2, color='g', linestyle=' ', marker='o', label='Comparable art product of the author -К')
        plt.plot(xData2, y1Data2, color='g', linewidth=2, label='Approximation of hyperbola y=(a/x)+b')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()

    elif mr == 1:  # построение графика для любого загруженного документа

        fig.clear(True)
        ax.clear()

        plt.title('Distribution of frequencies of use of words in the text', size=14)
        plt.xlabel('Serial number of new words', size=14)
        plt.ylabel('Frequency of the use of new words', size=14)
        plt.plot(xData1, yData1, color='r', linestyle=' ', marker='o', label='Test art product of the author -К')
        plt.plot(xData1, y1Data1, color='r', linewidth=2, label='Approximation of hyperbola y=(a/x)+b')
        plt.plot(xData2, yData2, color='g', linestyle=' ', marker='o', label='Comparable art product of the author -К')
        plt.plot(xData2, y1Data2, color='g', linewidth=2, label='Approximation of hyperbola y=(a/x)+b')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()


def master_reader():
    print('this is master_reader')
    filename = fd.askopenfilename(filetypes=(("TXT files", "*.txt"),
                                             ("HTML files", "*.html;*.htm"),
                                             ("All files", "*.*"))
                                  )

    for enc0 in encodings:
        print(f'enc0...{enc0}')
        try:
            #  with open(filename, 'r', encoding=enc0) as f:
            f = open(filename, 'r', encoding=enc0)

            st0 = f.read()
            fsize = len(st0)
            print(f'>>>>>>>>>> {fsize} <<<<<<<<<<')
            st_byte = st0.encode(enc0)

        except Exception:
            # print(f'$$${filename}$$$enc0={enc0}$$$enc1={enc1}$$$ exception in block 0 $$$')
            f.close()
            if enc0 != encodings[-1]:
                continue
            else:
                st0 = None
                break

        for enc1 in encodings:

            print(f'enc1...{enc1}')
            try:
                st1 = st_byte.decode(enc1)
                print(f'***********  {fsize} ***************')

                iMR = 0
                while iMR < fsize:
                    if st0[iMR] == st1[iMR]:
                        print(f'{iMR} ____ {st0[iMR]}::{st1[iMR]} ____')
                        iMR += 1
                        if iMR == fsize:
                            enc1 = encodings[-1]
                            raise Exception
                    else:
                        raise Exception


            except Exception:
                # print(f'$$${filename}$$$enc0={enc0}$$$enc1={enc1}$$$ exception in block 1 $$$')

                if enc1 != encodings[-1]:
                    continue
                else:
                    break

        break

    if st0 != None:
        st = st0
        return st
    else:
        return None


def choice_text():  # загрузка документов из файлов в поля формы

    # ===============================================================================
    # Всё те же игры с кодировками. Прочитали из файла в буфер, декодировали
    # в байтовый буфер, из байтового буфера опять кодировка в буфер
    # (попытки кодировки), часть из которых кончается исключениями. И тогда эта
    # кодировка заменяется очередной кодировкой из списка кодировок.
    #
    # #st = f.read()
    # # now start iterating in our encodings tuple and try to
    # # decode the file
    # st_byte=st.encode('cp1251')
    # for enc in encodings:
    #         try:
    #                 # try to decode the file with the first encoding
    #                 # from the tuple.
    #                 # if it succeeds then it will reach break, so we
    #                 # will be out of the loop (something we want on
    #                 # success).
    #                 # the data variable will hold our decoded text
    #                 st = st_byte.decode(enc)
    #                 break
    #         except Exception:
    #                 # if the first encoding fail, then with the continue
    #                 # keyword will start again with the second encoding
    #                 # from the tuple an so on.... until it succeeds.
    #                 # if for some reason it reaches the last encoding of
    #                 # our tuple without success, then exit the program.
    #                 if enc == encodings[-1]:
    #                         sys.exit(1)
    #                 continue
    #         break
    # ===============================================================================

    try:

        print(f'%%%%%%%%%%%%%%%%% txt0 %%%%%%%%%%%%%%%%%')
        if len(txt0.get(1.0, END)) == 1:
            txt0.insert(END, master_reader())

        print(f'%%%%%%%%%%%%%%%%% txt1 %%%%%%%%%%%%%%%%%')
        if len(txt1.get(1.0, END)) == 1:
            txt1.insert(END, master_reader())

        print(f'%%%%%%%%%%%%%%%%% txt2 %%%%%%%%%%%%%%%%%')
        if len(txt2.get(1.0, END)) == 1:
            txt2.insert(END, master_reader())

        print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

    except:

        print('problem whith choice_text')
        pass


def array_text_1():  # чтение данных из поля

    if len(txt0.get(1.0, END)) != 1:
        u = txt0.get(1.0, END)
    else:
        txt3.insert(END, 'There are no text №1')
        return
    op = 1
    processing_subjects(u, op)


def array_text_2():  # чтение данных из поля

    if len(txt1.get(1.0, END)) != 1:
        u = txt1.get(1.0, END)
    else:
        txt3.insert(END, "There are no text №2")
        return
    op = 2
    processing_subjects(u, op)


def array_text_3():  # чтение данных из поля

    if len(txt2.get(1.0, END)) != 1:
        u = txt2.get(1.0, END)
    else:
        txt3.insert(END, "There are no text №3")
        return
    op = 3
    processing_subjects(u, op)


"""
Токенизация:
Что такое токенизация и зачем она для обработки естественного языка (NLP). 
Обработка естественного языка(NLP) используется для создания таких приложений,
как классификация текста, сентиментальный анализ, интеллектуальный чат-бот, 
языковой перевод и многие другие. Для достижения указанных целей применяется
текстовый шаблон.

Токенизация разделяет большое количество текста на более мелкие фрагменты (токены). 
Эти фрагменты или токены очень полезны для поиска закономерностей и рассматриваются 
в качестве основного шага для стемминга и лемматизации. 

Английский язык в качестве примера. 
Любое предложение.

My name is Jamie Clark.

Перед обработкой естественного языка нужно идентифицировать слова, 
составляющие строку символов. 
Токенизация является важным шагом для продолжения обработки 
естественного языка (NLP). Этот шаг необходим, поскольку фактическое 
значение текста можно интерпретировать путем анализа каждого слова, 
присутствующего в тексте. После выполнения токенизации в указанной 
выше строке получается результат:

[‘My’, ‘name’, ‘is’, ‘Jamie’, ‘Clark’]

Существуют различные варианты использования этой операции. 
Можно использовать токенизированную форму, чтобы:

- подсчитать общее количество слов в тексте;
- подсчитать частоту слова, то есть общее количество раз, 
	когда конкретное слово присутствует, и многое другое.

Источник: https://pythonpip.ru/osnovy/tokenizatsiya-python

Прежде всего, надо очистить неструктурированные текстовые данные 
перед переходом к этапу моделирования. 
Очистка данных включает несколько шагов. 
Эти шаги состоят в следующем:

= Токенизация слов
= Части предсказания речи для каждого токена
= Лемматизация текста 
= Стемминг текста
= Определение и удаление стоп-слов 
= многое другое.

стемминг и лемматизация как основные шаги для очистки текстовых данных
с помощью обработки естественного языка (NLP). 

Токенизация с использованием функции split()
Функция split() – один из основных методов разделения строк. 
Эта функция возвращает список строк после разделения предоставленной 
строки определенным разделителем. 
Функция split() по умолчанию разбивает строку в каждом пробеле. 

print(my_text.split())

Однако при необходимости можно указать разделитель.

print(my_text.split('.'))

использование функции split() с точкой(.) в качестве параметра, 
чтобы разбить абзац до точки. 
Основным недостатком использования функции split() является то, 
что функция принимает по одному параметру за раз. Следовательно, можно 
использовать только разделитель для разделения строки. Также
функция split() не рассматривает знаки препинания как отдельный фрагмент.

Токенизация с набором инструментов естественного языка NLTK
Набор инструментов для естественного языка, также известный как NLTK,
– это библиотека, написанная на Python. Набор инструментов 
для естественного языка(NLTK) – это сторонняя библиотека, которую можно установить.
Библиотека NLTK обычно используется для символьной и статистической обработки
естественного языка и хорошо работает с текстовыми данными.

В наборе средств естественного языка(NLTK) 
есть модуль с именем tokenize(). Этот модуль далее подразделяется
на две подкатегории: токенизация слов и токенизация предложений.

Word Tokenize: метод word_tokenize() используется для разделения строки
на токены или слова.
Sentence Tokenize: метод sent_tokenize() используется для разделения
строки или абзаца на предложения.

Токенизация с использованием RegEx(регулярных выражений) в Python
Регулярное выражение (RegEx), представляет собой особую последовательность символов,
которая позволяет находить или сопоставлять другие строки или наборы строк с помощью
этой последовательности в качестве шаблона.

Чтобы начать работу с RegEx в Python предоставляется библиотека re. 
Библиотека re – одна из предустановленных библиотек в Python.

Такие задачи, как классификация текста или фильтрация спама, 
используют NLP вместе с библиотеками глубокого обучения, (это уже не про нас) 
такими как Keras и Tensorflow.

Источник: https://pythonpip.ru/osnovy/tokenizatsiya-python

=========================================================================================

nltk.tokenize package
Submodules:
nltk.tokenize.api module
nltk.tokenize.casual module
nltk.tokenize.destructive module
nltk.tokenize.legality_principle module
nltk.tokenize.mwe module
nltk.tokenize.nist module
nltk.tokenize.punkt module
nltk.tokenize.regexp module
nltk.tokenize.repp module
nltk.tokenize.sexpr module
nltk.tokenize.simple module
nltk.tokenize.sonority_sequencing module
nltk.tokenize.stanford module
nltk.tokenize.stanford_segmenter module
nltk.tokenize.texttiling module
nltk.tokenize.toktok module
nltk.tokenize.treebank module
nltk.tokenize.util module
Module contents
NLTK Tokenizer Package

Tokenizers divide strings into lists of substrings. 
For example, tokenizers can be used to find the words
and punctuation in a string:

>>> from nltk.tokenize import word_tokenize
>>> s = '''Good muffins cost $3.88\nin New York. 
Please buy me ... two of them.\nThanks.'''
>>> word_tokenize(s) 

['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.',
'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']

This particular tokenizer requires the Punkt sentence tokenization 
models to be installed. 
NLTK also provides a simpler, regular-expression based tokenizer, 
which splits text on whitespace and punctuation:

>>> from nltk.tokenize import wordpunct_tokenize
>>> wordpunct_tokenize(s) 

['Good', 'muffins', 'cost', '$', '3', '.', '88', 'in', 'New', 'York', '.',
'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']

We can also operate at the level of sentences, 
using the sentence tokenizer directly as follows:

>>> from nltk.tokenize import sent_tokenize, word_tokenize
>>> sent_tokenize(s)

['Good muffins cost $3.88\nin New York.', 'Please buy me\ntwo of them.', 'Thanks.']
>>> [word_tokenize(t) for t in sent_tokenize(s)] 

[['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.'],
['Please', 'buy', 'me', 'two', 'of', 'them', '.'], ['Thanks', '.']]

Caution: when tokenizing a Unicode string, make sure you are not using an encoded version 
of the string (it may be necessary to decode it first, e.g. with s.decode("utf8").

NLTK tokenizers can produce token-spans, represented as tuples of integers
having the same semantics as string slices, to support efficient comparison of tokenizers. 
(These methods are implemented as generators.)

>>> from nltk.tokenize import WhitespaceTokenizer
>>> list(WhitespaceTokenizer().span_tokenize(s)) 

[(0, 4), (5, 12), (13, 17), (18, 23), (24, 26), (27, 30), (31, 36), (38, 44),
(45, 48), (49, 51), (52, 55), (56, 58), (59, 64), (66, 73)]

There are numerous ways to tokenize text. If you need more control over tokenization, 
see the other methods provided in this package.

For further information, please see Chapter 3 of the NLTK book.

nltk.tokenize.sent_tokenize(text, language='english')[source]
Return a sentence-tokenized copy of text, using NLTK’s recommended sentence tokenizer 
(currently PunktSentenceTokenizer for the specified language).

Parameters
text – text to split into sentences
language – the model name in the Punkt corpus

nltk.tokenize.word_tokenize(text, language='english', preserve_line=False)[source]
Return a tokenized copy of text, using NLTK’s recommended word tokenizer 
(currently an improved TreebankWordTokenizer along with PunktSentenceTokenizer 
for the specified language).

Parameters
text (str) – text to split into words

language (str) – the model name in the Punkt corpus

preserve_line (bool) – A flag to decide whether to sentence tokenize the text or not.

Лемматизация — это процесс преобразования слова в его базовую форму. 
Разница между стемминг (stemming) и лемматизацией заключается в том, 
что лемматизация учитывает контекст и преобразует слово в его значимую базовую форму, 
тогда как стемминг просто удаляет последние несколько символов, 
что часто приводит к неверному значению и орфографическим ошибкам.

=========================================================================================
"""


def processing_subjects(u, op):
    global fig, ax

    # определние жанра текста ( NLTK+corpusbrown)
    # To download a particular dataset/models, use the nltk.download() function,
    # e.g. if you are looking to download the punkt sentence tokenizer, use:
    #
    # $ python3
    # >>> import nltk
    # >>> nltk.download('punkt')
    # If you're unsure of which data/model you need, you can start out
    # with the basic list of data + models with:
    #
    # >>> import nltk
    # >>> nltk.download('popular')
    # It will download a list of "popular" resources, these includes:
    #
    # <collection id="popular" name="Popular packages">
    #       <item ref="cmudict" />
    #       <item ref="gazetteers" />
    #       <item ref="genesis" />
    #       <item ref="gutenberg" />
    #       <item ref="inaugural" />
    #       <item ref="movie_reviews" />
    #       <item ref="names" />
    #       <item ref="shakespeare" />
    #       <item ref="stopwords" />
    #       <item ref="treebank" />
    #       <item ref="twitter_samples" />
    #       <item ref="omw" />
    #       <item ref="wordnet" />
    #       <item ref="wordnet_ic" />
    #       <item ref="words" />
    #       <item ref="maxent_ne_chunker" />
    #       <item ref="punkt" />
    #       <item ref="snowball_data" />
    #       <item ref="averaged_perceptron_tagger" />
    #     </collection>

    # nltk.download('punkt') # ???
    # q = word_tokenize(u,'english', False)
    q = word_tokenize(u)
    qq = [w for w in q if len(w) > 2]

    # nltk.download('averaged_perceptron_tagger') # ???
    z = pos_tag(qq)
    m = [w[0].lower() for w in z if w[1] == "NN"]

    d = {}
    for w in m:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    pairs = list(d.items())
    pairs.sort(key=lambda x: x[1], reverse=True)
    modals = []  # массив для формирования результатов
    wq = 10

    for i in pairs[0:wq]:
        modals.append(i[0])

    # nltk.download('brown') # ???
    cfd = ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre)
    )

    # cfd - это объект ConditionalFreqDist
    #     We can access the corpus as a list of words, or a list of sentences
    #     (where each sentence is itself just a list of words).
    #     We can optionally specify particular categories or files to read.
    #     we need to obtain counts for each genre of interest.
    #     We'll use NLTK's support for conditional frequency distributions.
    #     These are presented systematically in 2.2, where we also unpick
    #     the following code line by line.
    #     For the moment, you can ignore the details and just concentrate on the output.
    #     Мы можем получить доступ к корпусу в виде списка слов или списка предложений.
    #     (где каждое предложение само по себе является просто списком слов).
    #     При желании мы можем указать определенные категории или файлы для чтения.
    #     нам нужно получить количество для каждого интересующего жанра.
    #     Мы будем использовать поддержку NLTK для условных частотных распределений.
    #     Они систематически представлены в 2.2, где мы также расшифровываем следующий
    #     код построчно.
    #     На данный момент можно игнорировать детали и просто сосредоточиться на выводе.
    #
    #     >> > cfd = nltk.ConditionalFreqDist(
    #         ...(genre, word)
    #         ... for genre in brown.categories()
    #         ... for word in brown.words(categories=genre))
    #
    #     >> > genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
    #     >> > modals = ['can', 'could', 'may', 'might', 'must', 'will']
    #     >> > cfd.tabulate(conditions=genres, samples=modals)
    #
    #                    can   could   may     might  must    will
    #    news            93    86      66      38     50      389
    #    religion        82    59      78      12     54      71
    #    hobbies         268   58      131     22     83      264
    #    science_fiction 16    49      4       12     8       16
    #    romance         74    193     11      51     45      43
    #    humor           16    30      8       8      9       13
    #
    # Observe that the most frequent modal in the news genre is will,
    # while the most frequent modal in the romance genre is could. Would you have predicted this?
    # The idea that word counts might distinguish genres will be taken up again in
    # chap-data-intensive.
    # Обратите внимание, что наиболее частым модальным словом в жанре новостей является will,
    # в то время как самый частый модальный глагол в романтическом жанре — это could.
    # Вы бы смогли это предсказать?
    # Мысль о том, что количество слов может различать жанры, будет снова рассмотрена в
    # chap-data-intensive.

    # файл для записи cfd результатов функции ConditionalFreqDist
    # Функция табулирования () отображает количество вхождений текста
    # в двухмерную таблицу и горизонтальную таблицу.
    sys.stdout = open('out.txt', 'w')
    cfd.tabulate(conditions=genres, samples=modals)
    sys.stdout.close()  # перенаправление потоков

    f = open('out.txt', 'r')
    w = f.read()
    txt3.insert(END, w)
    f.close()

    # записали, прочитали и потом ещё раз записали?
    # Что за фигня...
    # sys.stdout = open('out.txt', 'w')
    # cfd.tabulate(conditions=genres, samples=modals)
    # sys.stdout.close()
    # # =============================================

    f = open('out.txt', 'r')
    b = 0
    u = {}
    for i in f:
        b = b + 1
        if b >= 2:
            d = i.split()
            c = d[1:len(d)]
            e = [int(w) for w in c]
            u[d[0]] = sum(e)

    for key, val in u.items():
        if val == max(u.values()):
            tex = "Text № -%i- Theme-- %s. Concurrences- %i" % (op, key, val)

    txt3.insert(END, tex)
    txt3.insert(END, '\n')
    f.close()

    # cfd умеет рисовать? а в чём проблема... этот объект рисует по осям
    # conditions=genres, samples=modals значения, которые он понабирал ранее.
    #
    # ConditionalFreqDist: часто используемые функции
    #
    # keys () # Получить значения ключа объекта карты и вернуть массив
    # Получите 20 самых популярных слов в тексте
    # vocabulary = fdist.keys()
    # vocabulary[1:20]
    #
    # freq () # Частота идентификатора
    # Получить частоту слова кит
    # fdist.freq('whale') * 100
    #
    # Функция табулирования () отображает количество вхождений текста
    # в двухмерную таблицу и горизонтальную таблицу.
    # Функция сначала рисует наибольшую частоту выборок распределения частот.
    # Если вы предоставите в функцию параметр Integer P,
    # функция нарисует первые P идентификаторы.
    # Параметр накопительный используется, чтобы установить, является ли счет накопительным
    # fdist.tabulate(20, cumulative=True) # Нарисуйте первые 20 идентификаторов
    #                                     # и сложите количество вхождений
    #
    # Функция plot () рисует график, использование аналогично табличному.
    # fdist.plot(20, cumulativce=True)

    fig.clear(True)
    ax.clear()

    cfd.plot(conditions=genres, samples=modals)


# ========================================================================================
def close_win():
    global plt, root, fig, ax

    fig.clear(True)
    ax.clear()

    root.quit()
    root.destroy()

    plt.close()

    sys.exit(0)


# ========================================================================================

def start_win():
    # интерфейс пользователя =================================================================
    #           tkinter + меню + цветовая разметка текстов + центрирование формы

    global root
    root = Tk()

    global fig, ax
    fig, ax = plt.subplots()

    root.geometry('1000x700+50+50')
    root.title('The analysis of the art text')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 4  # центрирование формы
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 16  # центрирование формы
    root.wm_geometry("+%d+%d" % (x, y))  # центрирование формы

    main_menu = T.Menu(root)
    root.config(menu=main_menu)
    file_menu = T.Menu(main_menu)

    main_menu.add_cascade(label="The comparative analysis of the art texts", menu=file_menu)
    file_menu.add_command(label="Choice of the texts", command=choice_text)
    file_menu.add_command(label="Definition of subjects of the text-1", command=array_text_1)
    file_menu.add_command(label="Definition of subjects of the text-2", command=array_text_2)
    file_menu.add_command(label="Definition of subjects of the text-3", command=array_text_3)
    file_menu.add_command(label="Definition of the author of the text", command=comor_text)
    file_menu.add_command(label="Exit from the program", command=close_win)

    lab = T.Label(root, text="The text for comparison  author -K ",
                  font=("Arial", 12, "bold "), foreground='red')
    lab.pack()

    global txt0
    txt0 = T.Text(root, width=100, height=5,
                  font=("Arial", 12), foreground='red', wrap=tkinter.WORD)
    txt0.pack()

    lab1 = T.Label(root, text="The test  author -K",
                   font=("Arial", 12, "bold "), foreground='green')
    lab1.pack()

    global txt1
    txt1 = T.Text(root, width=100, height=5,
                  font=("Arial", 12), foreground='green', wrap=tkinter.WORD)
    txt1.pack()

    lab2 = T.Label(root, text="The text  author-M",
                   font=("Arial", 12, "bold "), foreground='blue')
    lab2.pack()

    global txt2
    txt2 = T.Text(root, width=100, height=5,
                  font=("Arial", 12), foreground='blue', wrap=tkinter.WORD)
    txt2.pack()

    lab3 = T.Label(root, text="Text results of comparison",
                   font=("Arial", 12, "bold"), foreground='black')
    lab3.pack()

    global txt3
    txt3 = T.Text(root, width=100, height=6,
                  font=("Arial", 12), foreground='black', wrap=tkinter.WORD)
    txt3.pack()

    lab4 = T.Label(root, text="Minimum quantity of words in a window ",
                   font=("Arial", 12, "bold"), foreground='black')
    lab4.pack()

    global txt4
    txt4 = T.Text(root, width=8, height=1,
                  font=("Arial", 12), foreground='black', wrap=tkinter.WORD)

    wd = 10
    txt4.pack()
    txt4.insert(END, str(wd))

    lab5 = T.Label(root, text="Maximum quantity of words in a window ",
                   font=("Arial", 12, "bold"), foreground='black')
    lab5.pack()

    global txt5
    txt5 = T.Text(root, width=8, height=1,
                  font=("Arial", 12), foreground='black', wrap=tkinter.WORD)
    wd = 90
    txt5.pack()
    txt5.insert(END, str(wd))

    # ===================================================================================

    root.mainloop()

# =======================================================================================
