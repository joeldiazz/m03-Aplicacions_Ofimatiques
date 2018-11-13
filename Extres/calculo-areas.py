#Python 3.6#
"""Calculo de areas"""
#Coding: Utf-8
figura = input("¿Qué figura quiere calcular? Triangulo (T) o Circulo (C): ")
if(figura == "T"):
    base = int(input("Escriba la base: "))
    altura = int(input("Escriba la altura: "))
    areat= ((base * altura)/2)
    print("Un triángulo de base",base,"y altura",altura,"tiene un area de",areat,"")
elif(figura == "C"):
    radio = int(input("Escriba el radio: "))
    areac = (3.14*(radio*radio))
    print("Un circulo de radio",radio,"tiene un area de",areac,"")
else:
    print("Has de posar T o C.")
