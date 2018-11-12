#Python 3.6#
"""Si tiene entre 18 y 23 años (ambos incluídos) le decimos que puede entrar en la sesión de jóvenes."""
#Coding: Utf-8
edad= int(input("Indique su edad: "))
if(edad <= 23 and edad >= 18):
          print("Puede entrar en la sesión de jovenes!")
else:
          print("No puedes entrar a la sesión de jovenes con",edad,"años.")
