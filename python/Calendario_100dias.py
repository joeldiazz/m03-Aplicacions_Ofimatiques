##Python 3.6##
#coding:utf-8
"""Cada 100 dias mensaje"""
for dia in range(0,365):
    print(dia+1)
    if dia%365==100-1:
        print("Primeros 100 Días!!!")
    if dia%365==200-1:
        print("Muy bien sigue asi!! Ya 200")
    if dia%365==300-1:
        print("Enhorabuena por tus 300 días ya queda poco!")
    if dia%365==365-1:
        print("El año a acabado!")
