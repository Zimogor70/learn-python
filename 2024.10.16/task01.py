"""
Задача 2024.10.16.01

Написать функцию для генерации строки из n строчных латинских букв
"""

from random import randint
import string

def genStr(n:int)->str:
    g_str:str = ''
    let = string.ascii_letters
    for i in range(0,n):        
        g_str+=let[(randint(0,len(let)-1))]
    return g_str

def main()->None:
    print(genStr(15))

if __name__ == '__main__':  
    main()
