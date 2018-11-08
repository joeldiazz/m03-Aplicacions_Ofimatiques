              ##Python 3.6##
                 """3 Numeros ordenats de menor a mayor"""
#Coding: Utf-8
num1=int(input("1.Posa un nombre enter: "))
num2=int(input("2.Posa un nombre enter: "))
num3=int(input("3.Posa un nombre enter: "))
if(num3 <= num2 and num2 <= num1):
    print("",num3,",",num2,",",num1,"")
elif(num3 >= num2 and num2 >= num1):
    print("",num1,",",num2,",",num3,"")
elif(num2 <= num1 and num1 <= num3):
    print("",num2,",",num1,",",num3,"")
elif(num1 >= num3 and num3 >= num2):
    print("",num2,",",num3,",",num1,"")
elif(num2 >= num1 and num1 >= num3):
    print("",num3,",",num1,",",num2,"")
elif(num2 >= num3 and num3 >= num1):
    print("",num1,",",num3,",",num2,"")
print("(Ordenats de menor a mayor)")

***********************************************************
                      ##Python 3.6##
         """3 Numeros ordenados de menor a mayor sin IF"""
##Creditos Ian##
#coding:utf-8##
numeros=list(eval(input("Posa tres numeros separats per comes: ")))
numeros.sort()
print(numeros)
