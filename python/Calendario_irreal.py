##Python 3.6##
#coding:utf-8
"""Calendario Año irreal (Cada mes 30 días, año 360 días)"""
print("Mes 1")
for dia in range(0,360):
    print(dia+1)
    if (dia%360==30-1):
        print("Mes 2")
    if (dia%360==60-1):
        print("Mes 3")
    if (dia%360==90-1):
        print("Mes 4")
    if (dia%360==120-1):
        print("Mes 5")
    if (dia%360==150-1):
        print("Mes 6")
    if (dia%360==180-1):
        print("Mes 7")
    if (dia%360==210-1):
        print("Mes 8")
    if (dia%360==240-1):
        print("Mes 9")
    if (dia%360==270-1):
        print("Mes 10")
    if (dia%360==300-1):
        print("Mes 11")
    if (dia%360==330-1):
        print("Mes 12")
