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
            
#Python 3.6#
"""Números pares e impares un solo if"""
numero = int(input("Pon un número: "))
if((numero <0 )or(numero %2 == 0)or(numero >= -10) and (numero <=40)):
    print:("Este numero esta entre -10 y 40 o es negativo o es un numero par")
else:
print("El numero no esta dentro de los parametros (entre -10 y 40 o par o negativo)")
