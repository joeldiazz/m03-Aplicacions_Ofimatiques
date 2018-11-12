#Python 3.6#
"""Si tiene entre 15 y 17 años (ambos incluidos) pueden entrar en la sesión de tarde."""
#Coding: Utf-8
edad= int(input("Indique su edad: "))
if(edad <= 17 and edad >= 15):
          print("Puede entrar en la sesión de tarde!")
else:
          print("No puedes entrar a la sesión de tarde con",edad,"años.")
