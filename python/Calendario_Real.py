##Python 3.6##
#coding:utf-8
"""Calendario Año Real no bisiesto (365 días)"""
print("Enero!")
for dia in range(0,365):
    print(dia+1)
    if (dia%365==31-1):
        print("Febrero!")
    if (dia%365==59-1):
        print("Marzo!")
    if (dia%365==90-1):
        print("Abril!")
    if (dia%365==120-1):
        print("Mayo!")
    if (dia%365==151-1):
        print("Junio!")
    if (dia%365==182-1):
        print("Julio!")
    if (dia%365==212-1):
        print("Agosto!")
    if (dia%365==242-1):
        print("Setiembre!")
    if (dia%365==273-1):
        print("Octubre!")
    if (dia%365==303-1):
        print("Noviembre!")
    if (dia%365==334-1):
        print("Diciembre!")
