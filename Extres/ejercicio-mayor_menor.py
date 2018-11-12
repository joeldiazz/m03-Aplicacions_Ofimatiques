#Python 3.6#
"""COMPARADOR DE TRES NÚMEROS"""
#Coding: Utf-8
numero1= int(input("1.Pon un numero: "))
numero2= int(input("2.Pon un numero: "))
numero3= int(input("3.Pon un numero: "))
if(numero1 == numero2 and numero3 == numero2):
    print("Los 3 numeros (",numero1,",",numero2,"y",numero3,") que has escrito son iguales")
elif(numero1 == numero2 and (numero2 >= numero3 or numero2 <= numero3)):
    print("Dos de los números son iguales (",numero1,"y",numero2,")")
elif(numero3 == numero2 and (numero2 >= numero1 or numero2 <= numero1)):
    print("Dos de los números son iguales (",numero3,"y",numero2,")")
elif(numero1 == numero3 and (numero2 >= numero3 or numero2 <= numero3)):
    print("Dos de los números son iguales (",numero1,"y",numero3,")")
elif((numero2 >= numero3 or numero2 <= numero3)and(numero1 >= numero3 or numero1 <= numero3)):
     print("Ninguno de los numeros se repite.")
