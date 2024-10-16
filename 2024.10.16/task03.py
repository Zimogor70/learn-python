"""
Задача 2024.10.16.03

Написать функцию для генерации строки из n строчных и заглавных латинских букв, 
а также числе и символов

Заглавные должны добавляться в строку только
 если параметр use_uppercase в функции равен True.

А если параметр use_uppercase не указан при использовании функции,
 то генерируем строку только из строчных букв.

По тому же сценарию добавляем контроль использования цифр и символов
"""

from random import randint
import string

def str_Upper()->str:
    return string.ascii_uppercase

def str_Digits()->str:
    return string.digits

def str_Symbols()->str:
    return string.punctuation

def genStr(n:int , use_uppercase:bool = False,
                   use_digit:bool = False,
                   use_symbol:bool = False)->str:
    g_str:str = ''
    let = string.ascii_lowercase
    if use_uppercase: let+=str_Upper()
    if use_digit: let+=str_Digits()
    if use_symbol: let+=str_Symbols()

    for i in range(0,n): g_str+= let[(randint(0,len(let)-1))]         
    return g_str

def main()->None:
    print(genStr(15,True,True,True))

if __name__ == '__main__':
    main()