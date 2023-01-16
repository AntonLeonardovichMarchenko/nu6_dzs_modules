import shutil

filename1 = 'multi.txt'
filename2 = 'multiZ.txt'

def test():
    print('this is Copy File')
    copy(filename1, filename2)

def copy(filename1, filename2):

    fileA = open(filename1, 'rb')

    fileB = open(filename2, 'wb')
    shutil.copyfileobj(fileA, fileB)


    # Источник: https: // tonais.ru / file / kopirovanie - faylov - v - python?ysclid = lchpld6ugb537021930
