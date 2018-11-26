##Python 3.6##
#coding:utf-8
"""Calendario Año Real bisiesto (366 días)"""
print("Enero!")
for dia in range(0,366):
    print(dia+1)
    if (dia%366==31-1):
        print("Febrero!")
    if (dia%366==60-1):
        print("Marzo!")
    if (dia%366==91-1):
        print("Abril!")
    if (dia%366==121-1):
        print("Mayo!")
    if (dia%366==152-1):
        print("Junio!")
    if (dia%366==182-1):
        print("Julio!")
    if (dia%366==213-1):
        print("Agosto!")
    if (dia%366==244-1):
        print("Setiembre!")
    if (dia%366==274-1):
        print("Octubre!")
    if (dia%366==305-1):
        print("Noviembre!")
    if (dia%366==335-1):
        print("Diciembre!")
