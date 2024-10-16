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

def genStr(n:int , use_uppercase:bool = False, use_digit:bool = False)->str:
    g_str:str = ''
    let = ''
    if use_uppercase and use_digit:
        let = string.digits + string.ascii_letters
    elif use_uppercase:
        let = string.ascii_letters
    elif use_digit:
        let = string.ascii_lowercase + string.digits
    else:
        let = string.ascii_lowercase

    for i in range(0,n): g_str+= let[(randint(0,len(let)-1))]         
    return g_str

def main()->None:
    print(genStr(15,True))

if __name__ == '__main__':
    main()