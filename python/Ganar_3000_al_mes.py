## Python 3.6 ##
"""Cómo ganar 3000€ al mes netos?"""
    
#Coding: utf-8
M01= int(input("Qué nota has sacado en M01?"))
M02= int(input("Qué nota has sacado en M02?"))
M03= int(input("Qué nota has sacado en M03?"))
M04= int(input("Qué nota has sacado en M04?"))
M05= int(input("Qué nota has sacado en M05?"))
Loteria= input("Has ganado la loteria? Si o No")
Casarse= input("Te casas con un(a) milloneti?(de 80 años con problemas del corazón")
if(Loteria == "Si"):
     print("Tienes mucho dinero! No necesitas trabajar.")
else:
    if(Casarse == "Si"):
        print("Vives del cuento, no necesitas trabajar")
    else:
        if (M01 >= 9 and M02 >= 10 and M03 >= 8 and (M05 <= 8 and M05 >= 6)):
            print("Ganas 3.000€ netos al mes!")
        else:
            Ponderada=((M01*0.3)+(M02*0.4)+(M03*0.25)+(M05*0.05))
            if(Ponderada >= 8)
                print("Ganas 3.000€ netos al mes!")
            else:
                print("Morirás pobre.")
            
