#Python 3.6#
"""Números pares e impares"""
#Coding: Utf-8
numero= int(input("Pon un numero: "))
if(numero%2 == 0):
    if(numero >= -10 and numero <= 40):
        if(numero <= 0):
            print("Este número es par, esta entre -10 y 40 y es negativo")
        else:
            print("Este número es par, esta entre -10 y 40 y es positivo")
    else:
        if(numero <=0):
            print("Este número es par, NO esta entre -10 y 40 y es negativo")
        else:
            print("Este número es par, NO esta entre -10 y 40 y es positivo")
else:
    if(numero >= -10 and numero <= 40):
        if(numero <= 0):
            print("Este número es impar, esta entre -10 y 40 y es negativo")
        else:
            print("Este número es impar, esta entre -10 y 40 y es positivo")
    else:
        if(numero <=0):
            print("Este número es impar, NO esta entre -10 y 40 y es negativo")
        else:
            print("Este número es impar, NO esta entre -10 y 40 y es positivo")

