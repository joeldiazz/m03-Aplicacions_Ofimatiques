#Coding: utf-8
M01= int(input("Qué nota has sacado en M01?"))
M02= int(input("Qué nota has sacado en M02?"))
M03= int(input("Qué nota has sacado en M03?"))
M04= int(input("Qué nota has sacado en M04?"))
M05= int(input("Qué nota has sacado en M05?"))
Loteria= input("Has ganado la loteria? Si o No")
Casarse= input("Te casas con un(a) milloneti?(de 80 años con problemas del corazón")
if (M01 >= 9 and M02 >= 10 and M03 >= 8 and (M05 <= 8 and M05 >= 6)):
    print("Ganas 3.000€ netos al mes! Tu media ponderada es superior al 8.")
else:
    if(Loteria == "Si"):
        print("Tienes mucho dinero! No necesitas trabajar.")
    else:
        if(Casarse == "Si"):
            print("No necesitas trabajar, tienes mucho dinero.")
        else:
            print("Moriras pobre.")
