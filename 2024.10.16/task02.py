"""
Задача 2024.10.16.02

Написать функцию для генерации строки из n строчных и заглавных латинских букв
Заглавные должны добавляться в строку 
только если параметр use_uppercase в функции равен True.
А если параметр use_uppercase не указан при использовании функции, 
то генерируем строку только из строчных букв.
"""

from random import randint
import string

def genAllChars(n:int)->str:
    g_str:str = ''
    let = string.ascii_letters
    for i in range(0,n): g_str+= let[(randint(0,len(let)-1))]
    return g_str

def genLowChars(n:int)->str:
    g_str:str = ''
    let = string.ascii_lowercase
    for i in range(0,n): g_str+= let[(randint(0,len(let)-1))]            
    return g_str

def genStr(n:int , use_uppercase:bool = False)->str:
    if use_uppercase: return genAllChars(n)
    else: return genLowChars(n)   

def main()->None:
    print(genStr(15,True))

if __name__ == '__main__':  
    main()