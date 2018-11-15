
#Python 3.6#
"""Número Maxim 4 nombres"""
#Coding: Utf-8
num1 = float(input("1. Pon un número: "))
num2 = float(input("2. Pon un número: "))
num3 = float(input("3. Pon un número: "))
num4 = float(input("4. Pon un número: "))
if((num1 >= num2 and num2 >= num3 and num2 >= num4 ) or (num1 >= num3 and num3 >= num2 and num3 >= num4 )or (num1 >= num4 and num4 >= num3 and num4 >= num2 )):
    print(num1)
if((num2 >= num1 and num1 >= num3 and num1 >= num4 ) or (num2 >= num3 and num3 >= num1 and num3 >= num4 )or (num2 >= num4 and num4 >= num3 and num4 >= num1 )):
    print(num2)
if((num3 >= num2 and num2 >= num1 and num2 >= num4 ) or (num3 >= num1 and num1 >= num2 and num1 >= num4 )or (num3 >= num4 and num4 >= num1 and num4 >= num2 )):
    print(num3)
else: 
    print(num4)
