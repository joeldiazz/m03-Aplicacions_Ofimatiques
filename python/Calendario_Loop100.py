##Python 3.6##
#coding:utf-8
"""Enter cada 100 dias"""
any = input("Tu año es Bisiesto: ")
if(any == "Si"):
    for dia in range(0,100):
        print(dia+1)
    if(dia%100==100-1):       
        print("Pulse Enter")
        input()
        for dia in range(100,200):
            print(dia+1)
    if(dia%200==200-1):       
        print("Pulse Enter")
        input()
        for dia in range(200,300):
            print(dia+1)
    if(dia%300==300-1):       
        print("Pulse Enter")
        input()
        for dia in range(300,365):
            print(dia+1)
elif(any == "No"):
    for dia in range(0,100):
        print(dia+1)
    if(dia%100==100-1):       
        print("Pulse Enter")
        input()
        for dia in range(100,200):
            print(dia+1)
    if(dia%200==200-1):       
        print("Pulse Enter")
        input()
        for dia in range(200,300):
            print(dia+1)
    if(dia%300==300-1):       
        print("Pulse Enter")
        input()
        for dia in range(300,366):
            print(dia+1)
else:
    print("Debes escribir Si o No")
