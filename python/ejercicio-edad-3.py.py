## Python 3.6 ##
"""Practica 3: Edat Sessio de Joves"""
#coding: Utf-8
edat = int(input("Quina edat tens?:"))
if (((edat <= 23)and(edat >= 18))or(edat == 17)) :
  print ("Pots entrar en la sessió de joves")
else:
  print ("No pots entrar en la sessió de joves")
